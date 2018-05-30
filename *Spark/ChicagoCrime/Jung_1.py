# Question 1 

import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
from pyspark.sql.functions import regexp_extract
from pyspark.sql.types import IntegerType
import matplotlib.pyplot as plt 

sc.setLogLevel("ERROR")

path = '/Users/inshique/Desktop/crimeFull.csv'
crime = sqlContext.read.format('com.databricks.spark.csv').options(header='true',inferschema='true').load(path)

# extract columns 
crime = crime.select("Date","ID","Year")

# extract month information from date column 
crime = crime.select("ID", "Year", regexp_extract('Date', '^[^/]*', 0).alias('Month'))

# convert month's data type from string to interger 
crime = crime.withColumn("Month", crime["Month"].cast(IntegerType()))

# final answer 
crime = crime.groupBy("Year","Month").count().groupBy("Month").avg('count').sort("Month")
crime.show()

# convert to pandas df 
crime_pd = crime.toPandas()

# extract axis 
x = crime_pd['Month']
y = crime_pd['avg(count)']

# plot 
plt.bar(x,y)
plt.title("Question 1 Histogram")
plt.xlabel("Month")
plt.ylabel("Average Count")
plt.show()