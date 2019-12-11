# Query Athena Table From SageMaker Notebook

https://aws.amazon.com/blogs/machine-learning/run-sql-queries-from-your-sagemaker-notebooks-using-amazon-athena/

Installation 

```py 
import sys
!{sys.executable} -m pip install PyAthena
```
Sample code 

```py 
from pyathena import connect
import pandas as pd
conn = connect(s3_staging_dir='<ATHENA QUERY RESULTS LOCATION>',
               region_name='<YOUR REGION, for example, us-west-2>')

df = pd.read_sql("SELECT * FROM athenaquery.<YOUR TABLE NAME> limit 8;", conn)
df
```
