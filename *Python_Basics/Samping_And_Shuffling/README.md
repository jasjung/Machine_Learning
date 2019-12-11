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

## Random 

- https://www.geeksforgeeks.org/python-random-sample-function/

```py
import random 
list1 = [1, 2, 3, 4, 5, 6]  
print("With list:", random.sample(list1, 3))
```

