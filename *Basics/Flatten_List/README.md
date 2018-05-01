# Flatten List

```
def flat_list(L):
    return [i for sublist in L for i in sublist]

flat_list([[3,5],[6,6]])

# [3, 5, 6, 6]
```