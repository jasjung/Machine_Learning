# Question 4 

sc.setLogLevel("ERROR")

from pyspark.sql.functions import * # explode,regexp_extract,col,year,month,dayofmonth,hour,date_format,count,sum
from pyspark.sql.types import IntegerType, FloatType, StringType
from pyspark.mllib.stat import Statistics

from datetime import datetime, date
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

# read data
path = '/Users/inshique/Desktop/crimeFull.csv'
crime = spark.read.csv(path, header = True)

# select date and Arrest, convert date to timestamp 
crimeDate = crime.select(unix_timestamp("Date","MM/dd/yyyy hh:mm:ss a").cast("timestamp").alias("timestamp"),"Arrest","Date")

# create year, month, hour, day from timestamp 
crimeDate = crimeDate.select(year("timestamp").alias("Year"), 
                      month("timestamp").alias("Month"),
                      dayofmonth("timestamp").alias("dayofmonth"),                                
                      hour("timestamp").alias("hour"),
                      date_format("timestamp","EEEE").alias("dayofweek"),
                      "Arrest","Date")

# convert Arrest to be integer where 1 = Arrested, 0 = Not Arrested so it's possible to sum and calculate rate 
crimeDate= crimeDate.select("*",crimeDate.Arrest.cast("boolean").cast("integer").alias("ArrestBool"))
crimeDate.show()

## time of the day 
crime_calc = crimeDate.groupby("hour").agg(count("Year").alias("count"),sum("ArrestBool").alias("totalArrest"))
# calculate the arrest rates 
crime_calc = crime_calc.withColumn("rate", col("totalArrest")/col("count")).sort("hour")
crime_calc.show(24)
# convert to pandas df 
q4_hour = crime_calc.toPandas()
# extract columns 
x = q4_hour.hour
y = q4_hour.rate
# plot 
plt.bar(x,y)
plt.title("Question 2 Hour")
plt.xlabel("Hour")
plt.ylabel("Arrest Rate")
plt.xticks(np.arange(0, 24, 1.0))
plt.show()

## day of the week 
# calculate total count and total arrests 
crime_calc = crimeDate.groupby("dayofweek").agg(count("Year").alias("count"),sum("ArrestBool").alias("totalArrest"))
# calculate the arrest rates 
crime_calc = crime_calc.withColumn("rate", col("totalArrest")/col("count")).sort("dayofweek")
crime_calc.show()
# convert to pandas 
q4_day = crime_calc.toPandas()
# reindex to have correct order of days 
q4_day = q4_day.reindex([1,5,6,4,0,2,3])
# extract columns 
x = q4_day.dayofweek
y = q4_day.rate
# plot 
labels = ["Mon", "Tue", "Wed",'Thur','Fri','Sat','Sun']
plt.bar(range(7), y, align='center')
plt.xticks(range(7), labels)
plt.title("Question 2 DayOfWeek")
plt.xlabel("DayOfWeek")
plt.ylabel("Arrest Rate")
plt.show()

## month 
# calculate total count and total arrests 
crime_calc = crimeDate.groupby("month").agg(count("Year").alias("count"),sum("ArrestBool").alias("totalArrest"))
# calculate the arrest rates 
crime_calc = crime_calc.withColumn("rate", col("totalArrest")/col("count")).sort("month")
crime_calc.show()
# convert to pandas df 
q4_month = crime_calc.toPandas()
# extract columns 
x = q4_month.month
y = q4_month.rate
# plot 
plt.bar(x,y)
plt.title("Question 2 Month")
plt.xlabel("Month")
plt.ylabel("Arrest Rate")
plt.xticks(np.arange(0, 13, 1.0))
plt.show()





