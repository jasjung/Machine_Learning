# OS Library 

## CD to Home Directory 

```py 
import os 
os.chdir(os.path.expanduser('~'))

# os.chdir('~/') will not work 
```

ref: https://stackoverflow.com/questions/41733251/os-chdir-to-relative-home-directory-home-usr



## Run Command Line 

- https://unix.stackexchange.com/questions/238180/execute-shell-commands-in-python

Example of running `ls` command from python shell. 

```py 
import os
os.system('ls')
```