# Dict to Pandas DF 

```py
data = {'row_1': [3, 2, 1, 0], 'row_2': ['a', 'b', 'c', 'd']}

pd.DataFrame.from_dict(data, orient='index')

```

Ref: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.from_dict.html