# Convert Pandas DF to Spark DF 

This is useful for local development. 

```py 
import findspark
findspark.find() 

from pyspark import SparkContext
sc = SparkContext()

from pyspark.sql import SQLContext
sqlcontext = SQLContext(sc)

from pyspark.sql.types import *

schema = "col1,col2,col3"
fields = [StructField(field_name, StringType(), True) for field_name in schema.split(',')]
schema = StructType(fields)
sdf = sqlcontext.createDataFrame(df[['col1','col2','col3']].head(10),schema)
```

## Example from Spark Documentation 

http://spark.apache.org/docs/latest/sql-programming-guide.html#inferring-the-schema-using-reflection

```py
# Import data types
from pyspark.sql.types import *

sc = spark.sparkContext

# Load a text file and convert each line to a Row.
lines = sc.textFile("examples/src/main/resources/people.txt")
parts = lines.map(lambda l: l.split(","))
# Each line is converted to a tuple.
people = parts.map(lambda p: (p[0], p[1].strip()))

# The schema is encoded in a string.
schemaString = "name age"

fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
schema = StructType(fields)

# Apply the schema to the RDD.
schemaPeople = spark.createDataFrame(people, schema)

# Creates a temporary view using the DataFrame
schemaPeople.createOrReplaceTempView("people")

# SQL can be run over DataFrames that have been registered as a table.
results = spark.sql("SELECT name FROM people")

results.show()
# +-------+
# |   name|
# +-------+
# |Michael|
# |   Andy|
# | Justin|
# +-------+
```

## Simpler Method

```py 
pdf = pd.DataFrame({'value':["hi,hi",'what,is','testing,ok']})
sdf = sqlcontext.createDataFrame(pdf)
sdf.show()
+----------+
|     value|
+----------+
|     hi,hi|
|   what,is|
|testing,ok|
+----------+

# or 
sc.parallelize(["hi,hi",'what,is','testing,ok']).toDF(StringType()).show()
+----------+
|     value|
+----------+
|     hi,hi|
|   what,is|
|testing,ok|
+----------+
```