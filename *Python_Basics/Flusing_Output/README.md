# Flushing 

If you want a progress bar or status print from your loop, but do not want to output mutliple lines lines, you can flush the output so that only one row is printed. 

### Method 1: 

[Reference](https://stackoverflow.com/questions/6169217/replace-console-output-in-python)

```py
import sys 
for i in range(100):
    sys.stdout.write("\rDoing thing %i" % i)
    sys.stdout.flush()
```

### Method 2: 
[Reference](https://www.reddit.com/r/Python/comments/4v6d02/replacing_console_output/)

Instead of outputting a newline character \n at the end of the line, you can use a `\r`, which takes you back to the beginning of the line.

```py 
for i in range(100):
    print(i,flush=True,end='\r')
```

## Example 

If you want to output percentage completion:

```py 
for i in range(len(df)): 
    print('completed: %s %%' % (i/len(df)*100),flush=True,end='\r')  
    # ... 
```

```py 
for i in range(len(df)): 
    # print every 10 files
    if i % 10 == 0: 
        print('completed: %s %%' % (i/len(df)*100),flush=True,end='\r')  

    # ... 
```