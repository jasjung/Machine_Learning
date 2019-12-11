# Reload()

Reference

- https://gis.stackexchange.com/questions/201404/re-import-custom-functions-without-restarting-qgis
- https://stackoverflow.com/questions/961162/reloading-module-giving-nameerror-name-reload-is-not-defined

If I make changes to custom python function from another file, running `import your_module` does not reload the changes. That is when you use `reload` function. This is a built in function for python 2, but not for python 3. 

```py 
from imp import reload
import your_module
reload(your_module)
from your_module import your_function
your_function
```

