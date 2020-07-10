# SubString 

How to perform function like left() or right() on excel. 

Example: Table `t1` and `dt` (e.g. 2020-05-05) column 


```sql 
-- substr(<col name>,<start string index>,<end string index>)
SELECT 
	substr(dt,0,7) as dt 
FROM t1; 
```
