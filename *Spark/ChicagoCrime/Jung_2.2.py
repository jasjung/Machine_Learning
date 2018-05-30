# Question 2.2 

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


# convert Date column to datetime format 
crime_clean = crime_array.map(lambda x: (x[10].strip(), datetime.strptime(x[2],'%m/%d/%Y %I:%M:%S %p').date())).filter(lambda x: x[0].isdigit())

# filter to past 5 years # 2001 - 2015 -> 2015, 14 ,13 ,12 ,11 
crime_clean = crime_clean.filter(lambda x: x[1].year >= 2011 and x[1].year <= 2015)

# get tuple of (beat, year)
crime_pair = crime_clean.map(lambda x: (x[0],x[1].year))

# Map Reduce job -> key = (beat, year), value = (# of crimes)
crime_MR = crime_pair.map(lambda x: ((x[0],x[1]),1)).reduceByKey(lambda x,y: x+y)#.persist()

# extract distinct beats 
beats = crime_MR.map(lambda x: x[0][0]).distinct().sortBy(lambda x: x) 
## beats.count() # 303

# extract distinct years 
years = crime_MR.map(lambda x: x[0][1]).distinct().sortBy(lambda x: x ) 
## years.count() # 5 

# to calculate correlations compute all combinations of beats and years 
# ((beat, year), 0)
beatXyear = beats.cartesian(years).map(lambda x: (x,0)) 
## beatXyear.count() # 1515

# output = (index, beat)
beatDict = dict(beats.zipWithIndex().map(lambda x: (x[1],x[0])).collect())

# beatXyear = ((bear, year), 0)
# crime_MR  = ((bear, year), # of crimes)
# if crime_MR does not contain some combinations, join will show up as None
# output = ((beat, year),(0, # of crimes))
join = beatXyear.leftOuterJoin(crime_MR)
# replace None to 0 
join = join.map(lambda x: (x[0],0) if x[1][1] is None else (x[0],x[1][1]))
## join.collect() # ((beat, year), # of crimes)

# change format -> (year, (beat, crime))
join = join.map(lambda x: (x[0][1], (x[0][0],x[1])))
# groupby year 
crimeYear = join.groupByKey()
# sort by beat within value # 
crimeYear = crimeYear.map(lambda x: (x[0], sorted(x[1], key=lambda y: y[0])))
# drop beat column -> (year, (crime #1, #2, #3 ,...)) 
crimeYear = crimeYear.map(lambda x: (x[0], [y[1] for y in x[1]]))

# vectors -> year = row, beat = col 
crimeVector = crimeYear.map(lambda x: Vectors.dense(x[1]))

# compute correlation matrix
corr = Statistics.corr(crimeVector)
## corr.shape # (303,303)

# correlation dictionary function of the lower trinagle in the corr matrix 
def corrDictFunc(corr):
	# output = ((row, col): corr value)
	# corr.shape[0] = corr.shape[1]= 303 
	return dict(((i,j), corr[i][j]) for i in range(corr.shape[0]) for j in range(corr.shape[0]) if i<j)

corrDict = corrDictFunc(corr)

# find beats with highest correlations 
def topK(beat, index, k):
    keys = sorted(beat, key=beat.get, reverse=True)[:k]
    return [(index[x[0]], index[x[1]], beat[(x[0],x[1])]) for x in keys]

# display top 20 beat pairs 
topK(corrDict, beatDict, 20)



