# UDF and Pandas_UDF

Reference: 

- Official Documention Pandas UDF: [https://spark.apache.org/docs/2.3.0/sql-programming-guide.html#pandas-udfs-aka-vectorized-udfs](https://spark.apache.org/docs/2.3.0/sql-programming-guide.html#pandas-udfs-aka-vectorized-udfs)
- Decorator: [https://johnpaton.net/posts/clean-spark-udfs/](https://johnpaton.net/posts/clean-spark-udfs/)

```py 
import pandas as pd

from pyspark.sql.functions import col, pandas_udf
from pyspark.sql.types import LongType

# Declare the function and create the UDF
def multiply_func(a, b):
    return a * b

multiply = pandas_udf(multiply_func, returnType=LongType())

# The function for a pandas_udf should be able to execute with local Pandas data
x = pd.Series([1, 2, 3])
print(multiply_func(x, x))
# 0    1
# 1    4
# 2    9
# dtype: int64

# Create a Spark DataFrame, 'spark' is an existing SparkSession
df = spark.createDataFrame(pd.DataFrame(x, columns=["x"]))

# Execute function as a Spark vectorized UDF
df.select(multiply(col("x"), col("x"))).show()
# +-------------------+
# |multiply_func(x, x)|
# +-------------------+
# |                  1|
# |                  4|
# |                  9|
# +-------------------+
```
