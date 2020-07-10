# N-TILE 


If you want to group your data into N chunks, you can use ntile function. 


```sql 
select 
	NTILE(<N chunks>) OVER (ORDER BY <column to sort by> ASC) 
FROM ijung.sa_shopper_problem_count
; 
```

eg. 

```sql 
select 
	NTILE(10) OVER (ORDER BY col1 ASC) 
FROM t1; 
```


## If you want to do some stats by ntile 

```sql 
WITH tmp AS(
	SELECT 
		col0
		,NTILE(10) OVER (ORDER BY co1 ASC) AS ntile 
	FROM t1
)
SELECT 
	ntile
	,avg(col0)
FROM tmp 
GROUP BY ntile 
;
```