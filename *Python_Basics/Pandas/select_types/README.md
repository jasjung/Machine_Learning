# select types 

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.select_dtypes.html

Simple way to select columns by type 

```py
df.select_dtypes(include='number')
df.select_dtypes(include='object')
df.select_dtypes(include='bool')
```