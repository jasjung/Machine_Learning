# Between Patterns 

https://stackoverflow.com/questions/32680030/match-text-between-two-strings-with-regular-expression 

```py 
import re
s = 'Part 1. Part 2. Part 3 then more text'
re.search(r'Part 1(.*?)Part 3', s).group(1)
# '. Part 2. '
```
