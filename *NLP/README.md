# Text Mining 

## Useful Links 
### Startswith() 
- https://www.tutorialspoint.com/python/string_startswith.htm

```py
str = "this is good";
print (str.startswith( 'this' ))

# useful for finding certain columns 
cols = df.columns.values
cols[[i.startswith('c_') or i.startswith('i_') or i.startswith('b_') for i in cols]]
```

```py
# both pattern works. 
str.endswith(ex,'pattern')
# or
ex = 'hi.'
ex.endswith('pattern')
```

