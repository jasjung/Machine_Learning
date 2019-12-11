# Range 

ref: https://www.pythoncentral.io/pythons-range-function-explained/

Understanding basics of `Range()` Function. Range has three parameters: 

- `start`: Starting number of the sequence.
- `stop`: Generate numbers up to, but not including this number.
- `step`: Difference between each number in the sequence.

### Examples 

```py 
list(range(0, 10, 2))
# [0, 2, 4, 6, 8]

list(range(10, 0,-2))
# [10, 8, 6, 4, 2]

list(range(1,5))
# [1, 2, 3, 4]

list(range(5))  # same as list(range(0,5))
# [0, 1, 2, 3, 4]
```

That's it! 