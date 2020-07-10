# Reflect 

This function was used in dealing with PII data. It's a way of calling java function inside hive. 

https://cwiki.apache.org/confluence/display/Hive/ReflectUDF

Example 

```sql
SELECT reflect("java.lang.String", "valueOf", 1),
       reflect("java.lang.String", "isEmpty"),
       reflect("java.lang.Math", "max", 2, 3),
       reflect("java.lang.Math", "min", 2, 3),
       reflect("java.lang.Math", "round", 2.5),
       reflect("java.lang.Math", "exp", 1.0),
       reflect("java.lang.Math", "floor", 1.9)
FROM src LIMIT 1;
 
 
1   true    3   2   3   2.7182818284590455  1.0
```
