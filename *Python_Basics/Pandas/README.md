# Pandas 

## Groupby 

https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.core.groupby.DataFrameGroupBy.agg.html

```py 
>>> df = pd.DataFrame({'A': [1, 1, 2, 2],
...                    'B': [1, 2, 3, 4],
...                    'C': np.random.randn(4)})
```

```py 
df.groupby('A').B.agg(['min', 'max'])
```

Clean up index 

```py
t = df.groupby('A').B.agg(['min', 'max','mean'],as_index=False).reset_index()
```