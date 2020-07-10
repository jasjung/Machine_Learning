# XOR

Python Bitwise Operators

- https://www.w3schools.com/python/python_operators.asp
- https://kite.com/python/answers/how-to-use-the-xor-operator-in-python
- https://python-reference.readthedocs.io/en/latest/docs/operators/bitwise_XOR.html
- [Boolean Logic & Logic Gates: Crash Course Computer Science #3
](https://youtu.be/gI-qXk7XojA?t=474)


"XOR, also known as "exclusive or", compares two binary numbers bitwise. If both bits are the same, XOR outputs 0. If the bits are different, XOR outputs 1. For instance, performing XOR on 6 and 3 (binary 110 and 011, respectively) results in 5 (binary 101)." 

```
110
011 
---
101 
```


```
>>> bin(0b1111 ^ 0b1111)
'0b0'
>>> bin(0b1111 ^ 0b0000)
'0b1111'
>>> bin(0b0000 ^ 0b1111)
'0b1111'
>>> bin(0b1010 ^ 0b1111)
'0b101'
```

```
>>> # this example swaps integers without a temporary variable using XOR
>>> a = 2
>>> b = 8
>>> a ^= b
>>> b ^= a
>>> a ^= b
>>> a
8
>>> b
2
```


## Missing number 

https://stackoverflow.com/questions/50296429/unable-to-understand-the-logic-behind-xor-when-finding-the-missing-value-in-an
