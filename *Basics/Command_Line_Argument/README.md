# Command Line Argument 

Code on how to make your python code take input from command line. There are a few options. I wanted to do this because when I **auto push/pull git**, I wanted to provide the commit message from the command line. 

If you want to know what I'm talking about regarding, auto push/pull, see [here](https://github.com/jasjung/Python/tree/master/GitHub/Automatic_Push_Pull). 

Simplist method is using `sys` package. Then when you run the python code, simply type arguments after file name separated by a space. 
`python filename.py arg1 arg2 arg3`. 

```py
import sys 
print(sys.argv)
print(sys.argv[1] )
# out: arg1
```