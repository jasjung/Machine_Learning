# upload_from_CSV

- credit: https://www.youtube.com/watch?v=MOaXGYgqipQ

```py
import csv


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('your table')


def read_csv(path):
    L = []
    rows = csv.DictReader(open(path))
    for row in rows: 
        L.append(row)
    return L


def batch_write(table,rows):
    with table.batch_writer(overwrite_by_pkeys=['your partition key']) as batch:
        for row in rows: 
            batch.put_item(Item=row)
    return True 


path = 'data.csv'
rows = read_csv(path)
batch_write(table,rows)
```