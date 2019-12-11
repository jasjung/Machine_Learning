# Command Line Argument 

Code on how to make your python code take input from command line. There are a few options. I wanted to do this because when I **auto push/pull git**, I wanted to provide the commit message from the command line. 

If you want to know what I'm talking about regarding, auto push/pull, see [here](https://github.com/jasjung/Python/tree/master/GitHub/Automatic_Push_Pull). 

Simplist method is using `sys` package. Then when you run the python code, simply type arguments after file name separated by a space. 
`python filename.py arg1 arg2 arg3`. 

```py
import sys 
print(sys.argv)
print(sys.argv[1])
# out: arg1
```

## ARGPARSE 

```py
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
	help="name of the user")
args = vars(ap.parse_args())

# display a friendly message to the user
print("Hi there {}, it's nice to meet you!".format(args["name"]))
```

### Full Form 

```py
import argparse

def parse_arg():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--from", required=True, help="raw file path")
    ap.add_argument("-t", "--to", required=True, help="processed file path")
    args = vars(ap.parse_args())
    return args 

def main(args):
	... 

if __name__ == '__main__':
    args = parse_arg()
    main(args)
```