# Question 2.1 

sc.setLogLevel("ERROR")

from pyspark.sql.functions import * # explode,regexp_extract,col,year,month,dayofmonth,hour,date_format,count,sum
from pyspark.sql.types import IntegerType, FloatType, StringType
from pyspark.mllib.stat import Statistics

from datetime import datetime, date
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

# read in file 
path = '/Users/inshique/Desktop/crimeFull.csv'
crime = sc.textFile(path)

# remove header 
crime_array = crime.map(lambda line: line.split(',')).filter(lambda x: x[0] != "ID")

# convert Date column to datetime format 
crime_clean = crime_array.map(lambda x: (datetime.strptime(x[2],'%m/%d/%Y %I:%M:%S %p').date(),x[3]))

# filter the years to past 3 years 
crime_3yr = crime_clean.filter(lambda x: x[0].year >= 2013 and x[0].year <= 2015)     

# map reduce job 
output = crime_3yr.map(lambda x: (x[1],1)).reduceByKey(lambda x,y: int(x) + int(y))

# top 10 
output.map(lambda x: (x[1], x[0])).sortByKey(ascending = False).take(10)