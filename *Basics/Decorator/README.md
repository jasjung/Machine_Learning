# Decorator 

Reference: 

- [https://realpython.com/primer-on-python-decorators/#simple-decorators](https://realpython.com/primer-on-python-decorators/#simple-decorators) <- great tutorial! 

**"Decorators wrap a function, modifying its behavior."**

### Example 

```py 
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)

>>> say_whee()
Something is happening before the function is called.
Whee!
Something is happening after the function is called.
```
