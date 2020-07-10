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

Example of running `ls` command from python shell. But running this method in jupyter notebook will return 0. If you want to save output, use the `subprocess` package. 

```py 
import os
os.system('ls')
```

another method 

```py 
import subprocess 
output = subprocess.check_output("ls data".split(),universal_newlines=True)
# output = subprocess.check_output(['ls','data'],universal_newlines=True)
output.split()
```

## Recursive list dir 

https://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php

```py 
import os
path = "./TEST"

for root,d_names,f_names in os.walk(path):
	print root, d_names, f_names
```