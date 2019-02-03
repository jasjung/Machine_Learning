# Chinese Character 

Reference

- https://stackoverflow.com/questions/34587346/python-check-if-a-string-contains-chinese-character

```py
import re 
ipath= "./data/NCDC/上海/虹桥/9705626661750dat.txt" 
re.findall(r'[\u4e00-\u9fff]+', ipath) 
```

```py 
import re 
re.findall(r'[\u4e00-\u9fff]+', 'I live in 上海')
# Out[1]: ['上海']
```
