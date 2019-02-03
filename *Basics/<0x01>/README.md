# <0x01> Hidden Byte 

I had to read hive table file from hadoop but realized that there was a hidden byte delimitter. This is how I read it on python.  

```py 
pd.read_table(path,sep='\001')
```

