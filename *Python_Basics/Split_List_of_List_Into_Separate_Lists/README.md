# Seprate List of Lists into Seprate Lists 


Reference: https://stackoverflow.com/questions/16152957/separating-a-list-into-two-lists

```py 
L = [[1,2],[3,4],[5,6]]
l1,l2 = zip(*L)

print(l1) # (1, 3, 5)
print(l2) # (2, 4, 6)

type(l1) # tuple
type(list(l1)) # list
```
