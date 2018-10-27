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