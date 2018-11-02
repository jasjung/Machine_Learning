# Split()

```py
from pyspark.sql.types import *
# from pyspark.sql.functions import pandas_udf
from pyspark.sql.functions import col, pandas_udf, split

# in jupyternotebook
import findspark
findspark.find() 

from pyspark import SparkContext
sc = SparkContext()

from pyspark.sql import SQLContext
sqlcontext = SQLContext(sc)

print('Spark Version:',sc.version)

pdf = pd.DataFrame({'value':["hi,hi",'what,is','testing,ok']})

sdf = sqlcontext.createDataFrame(pdf)

tmp_split = split(sdf.value,',')

sdf = sdf.withColumn('c1', tmp_split.getItem(0))
sdf = sdf.withColumn('c2', tmp_split.getItem(1))
sdf.show()
```
