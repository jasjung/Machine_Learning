# Dummy Variable 

ref: 

- https://stackoverflow.com/questions/35879372/pyspark-matrix-with-dummy-variables
- https://stackoverflow.com/questions/38467763/spark-sql-select-all-and-computed-columns

This is a solution to do `pd.get_dummies` in PySpark dataframe. 


```py 
from pyspark.sql import functions as F

df = sqlContext.createDataFrame([
    (1, "a"),
    (2, "b"),
    (3, "c"),
], ["ID", "Text"])

categories = df.select("Text").distinct().rdd.flatMap(lambda x: x).collect()

exprs = [F.when(F.col("Text") == category, 1).otherwise(0).alias('Text_'+category)
         for category in categories]

df.select("ID", *exprs).show()
```


Output

```
+---+---+---+---+
| ID|  a|  b|  c|
+---+---+---+---+
|  1|  1|  0|  0|
|  2|  0|  1|  0|
|  3|  0|  0|  1|
+---+---+---+---+
```


Generalized Function 

```py 
def spark_dummy_var(col_name ): 
    categories = sdf.select(col_name).distinct().rdd.flatMap(lambda x: x).collect()
    exprs = [when(col(col_name) == category, 1).otherwise(0).alias(col_name+'_'+category)
             for category in categories]
    sdf.select(col_name, *exprs).show(3)
    
    # if you want to choose all columns 
    # sdf.select(col("*"),*exprs).show(3)
spark_dummy_var(col_name = 'communication_category')
```

```py
def spark_dummy_var(col_name):
    categories = sdf.select(col_name).distinct().rdd.flatMap(lambda x: x).collect()
    print(categories)

    dummy_cols = [col_name + '_' + i for i in categories]
    
    exprs = [when(col(col_name) == category, 1).otherwise(0).alias(col_name+'_'+category) for category in categories]
    tmp_df = sdf.select(col("*"),*exprs)#.show(3)
    return tmp_df, dummy_cols

sdf, dummy_cols = spark_dummy_var(col_name = 'c1')
sdf.select(dummy_cols).show()
```