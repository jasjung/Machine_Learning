# Timing 

## Timeit 

```py 
import timeit 
np.mean(timeit.repeat(lambda: "-".join(str(n) for n in range(100)), repeat=100,number=100))
```

`number`: how many times you want to repeat the lambda function 
`repeat`: how many times you want to repeat the lambda function after applying the number parameter. 


### Function 

from: https://www.geeksforgeeks.org/timeit-python-examples/

```py 
# importing the required module 
import timeit 
  
# code snippet to be executed only once 
mysetup = "from math import sqrt"
  
# code snippet whose execution time is to be measured 
mycode = ''' 
def example(): 
    mylist = [] 
    for x in range(100): 
        mylist.append(sqrt(x)) 
'''
  
# timeit statement 
print(timeit.timeit(setup=mysetup,stmt=mycode,number=10000))

# or repeat 
print(timeit.repeat(setup=mysetup,stmt=mycode,number=10000,repeat=3))
```


## Magic %time 

```py
%time print(1)
```

or 

```py 
%%time 
print(1)
```

The code above will show you how long the code took to run. 

## Time 

source: https://www.geeksforgeeks.org/time-perf_counter-function-in-python/

```py 
import time 
time.perf_counter()
```


```py 
# Python program to show time by perf_counter() 
from time import perf_counter 

# integer input from user, 2 input in single line 
n, m = map(int, input().split()) 

# Start the stopwatch / counter 
t1_start = perf_counter() 

for i in range(n): 
	t = int(input()) # user gave input n times 
	if t % m == 0: 
		print(t) 

# Stop the stopwatch / counter 
t1_stop = perf_counter() 

print("Elapsed time:", t1_stop, t1_start) 


print("Elapsed time during the whole program in seconds:", 
										t1_stop-t1_start) 

```

