# Question 2.3

sc.setLogLevel("ERROR")

from pyspark.sql.functions import * # explode,regexp_extract,col,year,month,dayofmonth,hour,date_format,count,sum
from pyspark.sql.types import IntegerType, FloatType, StringType
from pyspark.mllib.stat import Statistics
from pyspark.mllib.linalg import Matrices, Vectors

from datetime import datetime, date
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 


# load data 
path = '/Users/inshique/Desktop/crimeFull.csv'
crime = sc.textFile(path)

# remove header 
crime_array = crime.map(lambda line: line.split(',')).filter(lambda x: x[0] != "ID")

# extract (district, date)
crimes_clean = crime_array.map(lambda x: (x[11],datetime.strptime(x[2],'%m/%d/%Y %I:%M:%S %p').date()))

# remove erroneous districts that can occur due to csv issues 
crimes_clean = crimes_clean.filter(lambda x: len(x[0]) == 3).filter(lambda x: x[0].isdigit())

# Daley: April 24, 1989 – May 16, 2011
# Emanuel: May 16, 2011 – Present
daley = crimes_clean.filter(lambda x: x[1] < date(2011, 5, 16))  
emanuel =  crimes_clean.filter(lambda x: x[1] >= date(2011, 5, 16))

# group by district level  
daley_MR = daley.map(lambda x: (x[0],1)).reduceByKey(lambda x,y: x + y)
daley_month = daley.map(lambda x: x[1].strftime('%Y/%m')).distinct().count() 
emanuel_MR = emanuel.map(lambda x: (x[0],1)).reduceByKey(lambda x,y: x + y)
emanuel_month = emanuel.map(lambda x: x[1].strftime('%Y/%m')).distinct().count() 
## print(daley_month) 125 
## print(emanuel_month) 49 

# divide by the number of months to normalize 
daley_MR_avg = daley_MR.map(lambda x: (x[0],float(x[1])/daley_month))
emanuel_MR_avg = emanuel_MR.map(lambda x: (x[0],float(x[1])/emanuel_month))

# (district,(daley, emanuel))
join = daley_MR_avg.join(emanuel_MR_avg)
# daley - emanuel 
diff = join.map(lambda x: x[1][1] - x[1][0])

mean = diff.mean()
n = diff.count()
sd = diff.stdev()
sd_error = sd/np.sqrt(n)
t_test = mean/sd_error
t_test
# -5.350761841248918





