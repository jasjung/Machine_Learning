# When_Otherwise 

Method to change specific elements within pyspark dataframe. 

```py 
from pyspark.sql.functions import when   
df.withColumn('col_name', when(df.col_name.isnull(), 0).otherwise(df.col_name))
```

ref: https://datascience.stackexchange.com/questions/14648/replace-all-numeric-values-in-a-pyspark-dataframe-by-a-constant-value
