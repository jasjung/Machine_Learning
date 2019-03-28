# rank()

https://community.hortonworks.com/questions/24667/hive-top-n-records-within-a-group.html

- `parition by`: you can think of this as group by. 
- `value`: this is how you decide to order the rank. 

```sql
select * from (
	select user_id, value, desc, 
	rank() over ( partition by user_id order by value desc) as rank 
	from test4 ) t where rank < 3;
```
