# OS Library 

## CD to Home Directory 

```py 
import os 
os.chdir(os.path.expanduser('~'))

# os.chdir('~/') will not work 
```

ref: https://stackoverflow.com/questions/41733251/os-chdir-to-relative-home-directory-home-usr


