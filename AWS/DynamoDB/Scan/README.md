# Scan 

https://martinapugliese.github.io/interacting-with-a-dynamodb-via-boto3/

## Multiple Filters 

https://stackoverflow.com/questions/44704443/dynamodb-scan-using-filterexpression

```py 
import boto3
from boto3.dynamodb.conditions import Key, Attr, And 

filters = dict()
filters['Date'] = "2017-06-21"
filters['Shift'] = "3rd"

response = table.scan(FilterExpression=And(*[(Key(key).eq(value)) for key, value in filters.items()]))
```

v2 

```py
def add_expressions(expressions: dict):
    if len(expressions) > 1:
        return And(*[(Attr(key).eq(value)) for key, value in expressions.items()])
    elif len(expressions) == 1:
        return [(Attr(key).eq(value)) for key, value in expressions.items()][0] 
```


## Force Scan on All Items 

- https://stackoverflow.com/questions/43840225/full-table-scanning-using-boto3-python
- https://stackoverflow.com/questions/38386519/dynamodb-pagination-using-boto3
- https://stackoverflow.com/questions/36780856/complete-scan-of-dynamodb-with-%20boto3
- LastEvaluatedKey

