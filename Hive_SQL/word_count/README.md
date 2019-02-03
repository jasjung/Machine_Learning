# Word Count 

https://community.hortonworks.com/questions/64535/hive-wordcount.html

```sql 
SELECT word, count(1) AS count FROM
(SELECT explode(split(line, '\\s')) AS word FROM table) w
GROUP BY word
ORDER BY word;
```
