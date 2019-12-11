# Loading functions from different directory 

## v1 -> this is better

```py 
import os
import sys

sys.path.append('/Users/ijung/Python_Helpers/')

import your_function
```

## v2 

```py 
import os
import sys
# save current directory path 
dirPath = os.getcwd()
# cd to Python_Helpers Directory 
os.chdir(os.path.expanduser('~/Python_Helpers/'))

import your_function 

return to original path 
os.chdir(dirPath)
```
