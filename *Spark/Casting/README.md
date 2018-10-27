# Cast 

[ref](https://stackoverflow.com/questions/46956026/how-to-convert-column-with-string-type-to-int-form-in-pyspark-data-frame)

Convert spark dataframe column into different types. Eg. String to Integer 

```py 
from pyspark.sql.types import IntegerType
df = df.withColumn("col1", df["col1"].cast(IntegerType()))
```
