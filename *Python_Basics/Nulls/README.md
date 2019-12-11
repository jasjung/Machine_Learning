# Nulls 

How to deal with nulls in Python. 

## Numpy 

### Remove rows with nulls 
[Ref](https://stackoverflow.com/questions/11453141/how-to-remove-all-rows-in-a-numpy-ndarray-that-contain-non-numeric-values)

```py 
a = np.array([[1,2,3], [4,5,np.nan], [7,8,9]])
'''
array([[  1.,   2.,   3.],
       [  4.,   5.,  nan],
       [  7.,   8.,   9.]])
'''

a[~np.isnan(a).any(axis=1)]
'''
array([[ 1.,  2.,  3.],
       [ 7.,  8.,  9.]])
'''
```

### Check for nulls/inifinite 
[Ref](https://stackoverflow.com/questions/31323499/sklearn-error-valueerror-input-contains-nan-infinity-or-a-value-too-large-for)

```py 
# mat = np matrix 

# are there any nans?
np.isnan(mat)

# find their position 
np.where(np.isnan(mat))

# replace nan with zero 
np.nan_to_num(mat)
```

Going a bit further 

```py 
np.any(np.isnan(mat))
# and 
np.all(np.isfinite(mat))
```

## Pandas 

### Any rows with NAN

```py
df[df.isnull().any(axis=1)]

df.isnull().sum()

# filter it out 
df[~df.isnull().any(axis=1)]
```
 