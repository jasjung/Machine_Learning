# ApplyMap

ref: https://stackoverflow.com/questions/17950374/converting-a-column-within-pandas-dataframe-from-int-to-string

### Convert\_DF\_To_String

If for whatever reason you want to convert every cell in the dataframe into a string: 

```py 
df.applymap(str)
```

### Clipping 

```py 
df.applymap(lambda x: min(x,10))
```

### Convert Non Numeric Values to 0 in a DataFrame 

```py 
df.apply(lambda x: pd.to_numeric(x, errors='coerce').fillna(0))
```