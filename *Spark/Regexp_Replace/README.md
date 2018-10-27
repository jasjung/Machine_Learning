# regexp_replace

```py 
from pyspark.sql.functions import *
newDf = df.withColumn('address', regexp_replace('address', 'lane', 'ln'))
```

```
id     address
1       2 foo lane
2       10 bar lane
3       24 pants ln

--> 

id     address
1       2 foo ln
2       10 bar ln
3       24 pants ln
```

ref: https://stackoverflow.com/questions/37038014/pyspark-replace-strings-in-spark-dataframe-column