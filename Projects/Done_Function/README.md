# Done()

## Goal
Create a simple function that makes sound and returns current date and time. 

## Background 

I run a lot of models on jupyter notebook and they often take several minutes to hours. As a fun exercise, I wanted to build a `done` function that will chime and return date and time. This is so that I do not have to keep checking back on model to see if it's done and to know when the model finished running. 

Check out `done.py` to see my code. 

## How to Import 

For me, I placed this file under `Python_Helpers` directory in my home directory. So to call this function before I import other packages in Python, I simply run this from the beginning. 

```py
import os
# save current directory path 
dirPath = os.getcwd()
# cd to Python_Helpers Directory 
os.chdir(os.path.expanduser('~/Python_Helpers/'))
# import done function 
from done import done 
# return to original path 
os.chdir(dirPath)
```

## Music 
Remember to add your own sound and change the file name in `done.py`

## Additional Feature
If you want to see how long it took to run the model, you can put `%time`.  

