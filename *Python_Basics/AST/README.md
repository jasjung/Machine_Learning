# AST (Abstract Syntax Trees)

Convert string representation of list to list. 

From `"[1,2,3]"` to `[1,2,3]` 

```py
import ast 
ast.literal_eval("[1,2,3]")
# out [1,2,3]
```

Ref: https://stackoverflow.com/questions/1894269/convert-string-representation-of-list-to-list

You can also do 

```py
import json
json.loads("[1,2,3]")
# out [1, 2, 3]
```