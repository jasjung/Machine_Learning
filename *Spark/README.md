# Spark 

## Installation

### Method 1 (Use Method 2)

To install Spark to your Mac: [Click Here](https://medium.com/@GalarnykMichael/install-spark-on-mac-pyspark-453f395f240b)

You'll have to install Java JDK beforehand: [Click Here](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

- Check if Java is installed on mac: `javac -version`

This method works. However, `findspark` function was not working as I wanted. Second method works as expected and is cleaner. 

### Method 2 

Reference: [Click Here](https://medium.freecodecamp.org/installing-scala-and-apache-spark-on-mac-os-837ae57d283f)

```
# install java 
brew cask install java

# install spark 
brew install scala
brew install apache-spark

# to test 
spark-shell

# in jupyternotebook
import findspark
findspark.find() 

from pyspark import SparkContext
sc = SparkContext()

sc.parallelize(range(1000)).count()
# out: 1000 

```

- https://stackoverflow.com/questions/34601554/mac-spark-shell-error-initializing-sparkcontext?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

## SparkContext Error
When you spin up a new spark context in a new network (ie. you ran spark at work but now want to run it at home), run the following command in the command line and restart your kernel and spin up spark. 

```
sudo hostname -s 127.0.0.1
```

## GraphFrame
Reference: [Click Here](https://databricks.com/blog/2016/03/03/introducing-graphframes.html)


## Best Practices 

### ReduceByKey vs GroupByKey
Reference: [Click Here](databricks.gitbooks.io/databricks-spark-knowledge-base/content/best_practices/prefer_reducebykey_over_groupbykey.html)


## Reference 
- Spark2.3 - Pandas_UDF: https://databricks.com/blog/2017/10/30/introducing-vectorized-udfs-for-pyspark.html
- Spark2.2 - UDF: http://changhsinlee.com/pyspark-udf/
- UDF: https://databricks.com/blog/2017/10/30/introducing-vectorized-udfs-for-pyspark.html

## Deep Learning with Spark 
- https://docs.databricks.com/applications/deep-learning/spark-integration.html#deep-learning-spark-integration
- Keras: https://docs.databricks.com/applications/deep-learning/keras.html
- https://github.com/databricks/spark-deep-learning/blob/master/README.md#applying-deep-learning-models-at-scale


## Standardize All Features 
I had a problem where I wanted to process all columns in a dataframe similar to how I would use `from sklearn import preprocessing` function. The following function does just that using spark sql. There are other options but none of them standardized the dataframe at once. 

[Reference](https://stackoverflow.com/questions/47624129/how-to-standardize-one-column-in-spark-using-standardscaler?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)

```
import pyspark.sql.functions as func
from pyspark.sql.functions import stddev, mean, broadcast

# df_f = dataframe of interest 
# features you want to standardize in a dataframe 
cols = features 
stats = (df_f.groupBy().agg(
        *([stddev(x).alias(x + '_stddev') for x in cols] + 
          [mean(x).alias(x + '_avg') for x in cols])))

df = df_f.crossJoin(broadcast(stats))
exprs = [((df[x] - df[x + '_avg']) / df[x + '_stddev']).alias(x+'_scaled') for x in cols]

df_scaled = df.select([other columns you want to include]+exprs)
```

## Copying File to Executors 
```
path = 'file/location'
sc.sparkContext.addFile(path)
```
Then you can simply call that file from any map or udf functions by the name of the file. 

## Create Random Key 
```
import random 
# random.randint(1,1000)

# Use udf to define a row-at-a-time udf
@udf('integer')
def rand_key():
    return random.randint(1,100)
df = df.withColumn('key',rand_key())
```

## Convert bool string to int 
```
@udf('integer')
# Input/output are both a single double value
def convert_bool(b):
    if b =='true':
        return 1
    else:
        return 0
df = df.withColumn('bool',convert_bool('colum you want to convert')

```

## Mappartition 
[Reference](https://www.supergloo.com/fieldnotes/apache-spark-transformations-python-examples/#mapPartitions)

```
one_through_9 = range(1,10)
parallel = sc.parallelize(one_through_9, 3)
def f(iterator): yield sum(iterator)
parallel.mapPartitions(f).collect()
# [6, 15, 24]

parallel = sc.parallelize(one_through_9)
parallel.mapPartitions(f).collect()
# [1, 2, 3, 4, 5, 6, 7, 17]
```

Results [6,15,24] are created because mapPartitions loops through 3 partitions which is the second argument to the sc.parallelize call.

- Partition 1: 1+2+3 = 6
- Partition 2: 4+5+6 = 15
- Partition 3: 7+8+9 = 24
 
The second example produces [1,2,3,4,5,6,7,17] which I’m guessing means the default number of partitions on my laptop is 8.

- Partition 1 = 1
- Partition 2 = 2
- Partition 3 = 3
- Partition 4 = 4
- Partition 5 = 5
- Partition 6 = 6
- Partition 7 = 7
- Partition 8: 8+9 = 17

Typically you want 2-4 partitions for each CPU core in your cluster.

## VectorAssembler

Combine multiple columns into a single column as an array. 

```
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

features_to_combine = ['col1','col2','col3']

assembler = VectorAssembler(
    inputCols=features_to_combine,
    outputCol="features")

# combined columns will be named as 'features'

df = assembler.transform(df)
df.select('features').show(1)
```