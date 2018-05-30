# Question 4 

# import functions 
from pyspark.sql.functions import * # explode,regexp_extract,col,year,month,dayofmonth,hour,date_format,count,sum
from pyspark.sql.types import IntegerType, FloatType, StringType
from pyspark.mllib.stat import Statistics
from pyspark.sql.window import Window

from datetime import datetime, date
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

# read data
path = '/Users/inshique/Desktop/crimeFull.csv'
crime = spark.read.csv(path, header = True)

# select date and Arrest, convert date to timestamp 
crimeDate = crime.select(unix_timestamp("Date","MM/dd/yyyy hh:mm:ss a").cast("timestamp").alias("timestamp"),"Arrest","Date","Beat","IUCR")

# extract features 
crimeDate = crimeDate.select(year("timestamp").alias("Year"), 
                      month("timestamp").alias("Month"),
                      weekofyear("timestamp").alias("week"),
                      "*")

# create year+week column 
crimeDate = crimeDate.withColumn("yearweek", crimeDate.Year.cast(IntegerType())*100 +crimeDate.week.cast(IntegerType()))
# sort by yearweek column 
crimeDate = crimeDate.sort("yearweek")
# change Beat column into integer type. If not integer, remove the row 
crimeDate = crimeDate.withColumn("Beat", col("Beat").cast(IntegerType())).na.drop()

### 
# change IUCR column into integer type. If not integer, remove the row  
crimeDate = crimeDate.withColumn("IUCR", col("IUCR").cast(IntegerType())).na.drop()

# find the average of IUCR to split them 
# crimeDate.agg({'IUCR':'avg'}).collect()
# [Row(avg(IUCR)=1134.731230109342)]

# create crimeDegree columns 
crimeDate = crimeDate.withColumn('crimeDegree', col('IUCR')>=1034)

# separate the data into severe and minor crrimes
# crimeDegree = True = severe crime 
# crimeDegree = False = minor crime 
crimeSevere = crimeDate.filter("crimeDegree = true")
crimeMinor = crimeDate.filter("crimeDegree = false")
### 

# group by yearweek and beat to get beat level data 
# crimeWeek = crimeDate.groupBy("yearweek", "Beat").count()
crimeSevere = crimeSevere.groupBy("yearweek", "Beat").count()
crimeMinor = crimeMinor.groupBy("yearweek", "Beat").count()

# create lag columns 
def lag_generater(crimeWeek):
    crimeWeek = crimeWeek.select("*", lag("count").over(Window.orderBy("yearweek")).alias("count_lag1")).na.drop()
    crimeWeek = crimeWeek.select("*", lag("count_lag1").over(Window.orderBy("yearweek")).alias("count_lag2")).na.drop()
    crimeWeek = crimeWeek.select("*", lag("count_lag2").over(Window.orderBy("yearweek")).alias("count_lag3")).na.drop()
    crimeWeek = crimeWeek.select("*", lag("count_lag3").over(Window.orderBy("yearweek")).alias("count_lag4")).na.drop()
    crimeWeek = crimeWeek.withColumnRenamed("count", "label")
    return crimeWeek

crimeSevere = lag_generater(crimeSevere)
crimeMinor = lag_generater(crimeMinor)


# https://spark.apache.org/docs/2.1.0/mllib-ensembles.html#random-forests
# temp final 
# read temperature data 
path = '/Users/inshique/Desktop/temperature.csv'
temp = spark.read.csv(path, header = True)
# parse time 
tempDate = temp.select(unix_timestamp("Time","dd.MM.yyyy HH:mm").cast("timestamp").alias("timestamp"),"Temperature","Humidity")
# extract feature 
tempDate = tempDate.select(year("timestamp").alias("Year"), 
                      weekofyear("timestamp").alias("week"),
                      "*")
# creater yearweek column 
tempDate = tempDate.withColumn("yearweek", tempDate.Year.cast(IntegerType())*100 +tempDate.week.cast(IntegerType()))
tempDate = tempDate.sort("yearweek")
# extract columns 
tempDate = tempDate.select("yearweek","Temperature", "Humidity")

#crimeWeek = crimeDate.groupBy("yearweek", "Beat").count()
tempWeek = tempDate.groupBy("yearweek").agg({'Humidity':'avg', 'Temperature':'avg'})
tempWeek = tempWeek.select('yearweek',col('avg(Temperature)').alias('Temperature'), col('avg(Humidity)').alias('Humidity'))
#tempWeek.show()

#crimeJoined = crimeWeek.join(tempWeek, crimeWeek.yearweek == tempWeek.yearweek, 'inner')
#crimeJoined = crimeJoined.drop(tempWeek.yearweek)

#
crimeJoinedSevere = crimeSevere.join(tempWeek, crimeSevere.yearweek == tempWeek.yearweek, 'inner')
crimeJoinedSevere = crimeJoinedSevere.drop(tempWeek.yearweek)
#
crimeJoinedMinor = crimeMinor.join(tempWeek, crimeMinor.yearweek == tempWeek.yearweek, 'inner')
crimeJoinedMinor = crimeJoinedSevere.drop(tempWeek.yearweek)

## END of TEMP 

# RANDOM FOREST 

from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler

assembler = VectorAssembler(inputCols=['count_lag1','count_lag2',
                                       'count_lag3','count_lag4',
                                       'Temperature','Humidity'],
                            outputCol='features')

from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator

# Train a RandomForest model.
rf = RandomForestRegressor(numTrees=100)

# Chain indexer and forest in a Pipeline
pipeline = Pipeline(stages=[assembler, rf])

#(trainingData, testData) = crimeJoined.randomSplit([0.7, 0.3])
(trainingDataSevere, testDataSevere) = crimeJoinedSevere.randomSplit([0.7, 0.3])
(trainingDataMinor, testDataMinor) = crimeJoinedMinor.randomSplit([0.7, 0.3])

# Train model.  This also runs the indexer.
#model = pipeline.fit(trainingData)
modelSevere = pipeline.fit(trainingDataSevere)
modelMinor = pipeline.fit(trainingDataMinor)

# Make predictions.
#predictions = model.transform(testData) 
predictionsSevere = modelSevere.transform(testDataSevere) 
predictionsMinor = modelMinor.transform(testDataMinor) 

# show example rows 
#predictions.select("yearweek", "Beat", "features", "label", "prediction").show()
predictionsSevere.select("yearweek", "Beat", "features", "label", "prediction").show()
predictionsMinor.select("yearweek", "Beat", "features", "label", "prediction").show()

# Select (prediction, true label) and compute test error
evaluator = RegressionEvaluator(
    labelCol="label", predictionCol="prediction", metricName="rmse")
#rmse = evaluator.evaluate(predictions)
rmseSevere = evaluator.evaluate(predictionsSevere)
rmseMinor = evaluator.evaluate(predictionsMinor)
print("Root Mean Squared Error (RMSE) on testSevere data = %g" % rmseSevere)
print("Root Mean Squared Error (RMSE) on testMinor data = %g" % rmseMinor)

#Root Mean Squared Error (RMSE) on testSevere data = 5.92071
#Root Mean Squared Error (RMSE) on testMinor data = 5.99539

#### PREDICTING NEXT WEEK 
# extract the last week from our dataset
#crimeLastWeek = crimeJoined.filter(col("yearweek") == "201521")
crimeLastWeekSevere = crimeJoinedSevere.filter(col("yearweek") == "201521") 
crimeLastWeekMinor = crimeJoinedMinor.filter(col("yearweek") == "201521") 

# Make predictions.
#prediction_lastweek = model.transform(crimeLastWeek) 
prediction_lastweek_Severe = modelSevere.transform(crimeLastWeekSevere) 
prediction_lastweek_Minor = modelMinor.transform(crimeLastWeekMinor) 

# output of last week's prediction 
#prediction_lastweek.select("Beat", "features", "label", "prediction").show(300)
prediction_lastweek_Severe.select("Beat", "features", "label", "prediction").show(300)
prediction_lastweek_Minor.select("Beat", "features", "label", "prediction").show(300)





