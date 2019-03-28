# Explode 

`LATERAL VIEW EXPLODE`

Example: Given Table `tb`

|col1|col2|
|---|---|
| 1 |[a,b]|
| 2 |[a,c]|

---> table `explode_table`

|col1|explode_col|
|---|---|
| 1 |a|
| 1 |b|
| 2 |a|
| 2 |c|

```sql 
SELECT
	col1
	,explode_table.explode_col
FROM tb 
LATERAL VIEW EXPLODE(col2) explode_table AS explode_col

```
