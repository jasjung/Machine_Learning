# One Hot Encoding 

```py
pd.get_dummies()

pd.get_dummies([pd_series_here],prefix='communication_category')

# to join with existing table 
tmp = pd.get_dummies([pd_series_here],prefix='communication_category')
pd.concat([df,tmp],axis=1)
```

- https://machinelearningmastery.com/how-to-one-hot-encode-sequence-data-in-python/
- http://pbpython.com/categorical-encoding.html


```py 
col_to_convert
for i in col_to_convert:
    pd.get_dummies(tmp[i],prefix=i)
    df = df.drop([i],axis=1)
```