# Eval 

- https://realpython.com/python-eval-function/
- https://www.w3schools.com/python/ref_func_eval.asp

- dynamically evaluate expressions from a string-based or compiled-code-based input. 
- If you pass in a string to eval(), then the function parses it, compiles it to bytecode, and evaluates it as a Python expression.
- The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.



```py
eval(expression[, globals[, locals]])
```

Example 

```py 
x = 100  # A global variable
eval("x + 100", {"x": x})

x = 100  # A global variable
eval("x + 100")

# this will not work 
y = 200  # Another global variable
eval("x + y", {"x": x})


```
