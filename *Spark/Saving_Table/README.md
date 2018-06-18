# Saving Tables 

There are many ways of saving pyspark dataframe tables 

```
pyspark_DF.write.mode('overwrite').format('parquet').saveAsTable('table_name')

pyspark_DF.write.mode('append').format('parquet').saveAsTable('table_name')

# needed this for insertInto 
sqlContext.setConf("hive.exec.dynamic.partition.mode", "nonstrict")
pyspark_DF.write."insertInto('table_name')
```


References 

- [InsertInto Error](https://forums.databricks.com/questions/8555/ive-set-the-partition-mode-to-nonstrict-in-hive-bu.html)
