# pointers in python 

https://realpython.com/pointers-in-python/

Below are quotes and summaries from the link above. 


### In Python, everything is an object

```
>>> isinstance(1, object)
True
>>> isinstance(list(), object)
True
```

### Immutable vs Mutable Objects

- `id()`: returns the object’s memory address.
- `is`: returns True if and only if two objects have the same memory address.
- `Int` is immutable. Thus, `x = 5` and `x+= 1` will have different ID because you want to assign a new object with new address.
- `List` is mutable. 


### Understanding Variables

- Python variables are fundamentally different than variables in C or C++. In fact, Python doesn’t even have variables. Python has names, not variables.
- In C (`int x = 2337;`), `x` (variable) is the memory location, not just a name for it.
- In Python (`x = 2337`), `x` is bound to the PyObject reference. 
