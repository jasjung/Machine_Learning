# Sampling and Shuffling Data

## Pandas 

### Shuffle 

```py 
df = df.sample(frac=1)
```

### Sample 10%

```py 
df = df.sample(frac=.1)
```

## Numpy 

### Sample 

```py
A[np.random.choice(A.shape[0], num_rows_2_sample, replace=False)]
```