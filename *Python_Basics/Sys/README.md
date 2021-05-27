# Sys

- https://www.geeksforgeeks.org/take-input-from-stdin-in-python/
- https://www.askpython.com/python/python-stdin-stdout-stderr
- https://www.sanfoundry.com/python-questions-answers-sys-module/

## STDIN 

`sys.stdin`

```py 
import sys 

for line in sys.stdin: 
    if 'q' == line.rstrip(): 
        break
    print(f'Input : {line}') 
  
print("Exit") 


# v2 
import sys 
for x in sys.stdin:
# for x in sys.stdin.readline(): 
    print(x)


# v3 
# ctrl + d to finish reading 
lines = sys.stdin.readline()
lines = sys.stdin.readlines()
# reads the entire input as a single string  
inputs = sys.stdin.read()
```

### input vs sys.stdin

- https://www.geeksforgeeks.org/difference-between-input-and-sys-stdin-readline/

If user is inputting two lines, you can read the whole input using `readlines()` or one by one with `readline()` or `input()`. `input()` behaves similar to `readline()`

```py
# user input: 
## hello
## world 

print(input()) # hello
print(input()) # world 
print(input()) # throws error 

```



`readline(s)` will 


## STDOUT 

Writing to file 

https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print


```py 
import sys
temp = sys.stdout                 # store original stdout object for later
sys.stdout = open('log.txt', 'w') # redirect all prints to this log file
print("testing123")               # nothing appears at interactive prompt
print("another line")             # again nothing appears. it's written to log file instead
sys.stdout.close()                # ordinary file object
sys.stdout = temp                 # restore print commands to interactive prompt
print("back to normal")           # this shows up in the interactive prompt
``` 


Writing to console 

```py
import sys
stdout_fileno = sys.stdout
sample_input = ['Hi', 'test', 'test2']
 
for i in sample_input:
    # Prints to stdout
    stdout_fileno.write(i + '\n')
```

### Print vs STDOUT 

- https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print



## STDERROR 

This is similar to sys.stdout because it also prints directly to the Console. But the difference is that it only prints Exceptions and Error messages.


