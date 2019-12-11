# Reading File 

```py 
path = 'file.txt'
with open(path,'r') as f:
    df = f.readlines() 
    # or 
    # df = f.read() 
```

## Skip Row 

- https://stackoverflow.com/questions/4796764/read-file-from-line-2-or-skip-header-row

```py 
with open(fname) as f:
    next(f)
    for line in f:
        #do something
```