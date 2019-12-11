# Flatten List

```py 
def flat_list(L):
    return [i for sublist in L for i in sublist]

flat_list([[3,5],[6,6]])

# [3, 5, 6, 6]
```


Same as this: 

```py 
flat_list = []

for sublist in L: 
    print(sublist)
    for i in sublist: 
        print(i)
        flat_list.append(i)

print(flat_list)
```