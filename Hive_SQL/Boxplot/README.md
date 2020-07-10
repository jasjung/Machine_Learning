# Box plot / Quantiles

```sql 
SELECT 
	col1 
	,min(col2) AS min
	,percentile(col2, 0.25) AS Q1
	,percentile(col2, 0.5) AS median
	,avg(col2) AS avg
	,percentile(col2, 0.75) AS Q3
	,max(col2) AS max
		
FROM table
GROUP BY col1;
```