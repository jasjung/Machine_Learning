# Groupby_Concat

Link: https://stackoverflow.com/questions/17841149/pandas-groupby-how-to-get-a-union-of-strings?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

```
>>> d
   A       B
0  1    This
1  2      is
2  3       a
3  4  random
4  1  string
5  2       !

>>> d.groupby('A')['B'].apply(list)
A
1    [This, string]
2           [is, !]
3               [a]
4          [random]
dtype: object
```
