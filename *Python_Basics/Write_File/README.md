# Write to File 

- your object needs to be `string` when you write to a file. Simply convert by doing `str(<your_value>)`

## Append 

```py 
with open('<your_file.txt>', 'a') as f:
    f.write('something')
    f.write('\t')
    f.write('something2')
    f.write('\n')	
    ...
```


## Write 

```py 
with open('<your_file.txt>', 'w') as f:
    f.write('something')
    f.write('\t')
    f.write('something2')
    f.write('\n')	
    ...
```
