# Create Table From CSV

- https://docs.aws.amazon.com/athena/latest/ug/lazy-simple-serde.html
- https://docs.aws.amazon.com/athena/latest/ug/csv.html

NOTE: MAKE SURE LOCATION IS POINTING TO A DIRECTORY, NOT A FILE ITSELF. 

## Create 

The files do not actually have to be surrounded by quotes. 

```csv
"a1","a2","a3","a4"
"1","2","abc","def"
"a","a1","abc3","ab4"
```

```sql
CREATE EXTERNAL TABLE myopencsvtable (
   col1 string,
   col2 string,
   col3 string,
   col4 string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
   'separatorChar' = ',',
   'quoteChar' = '"',
   'escapeChar' = '\\'
   )
STORED AS TEXTFILE
LOCATION 's3://location/of/csv/';
```

## Delete 

```sql 
DROP TABLE IF EXISTS my_table;
``` 

## Method 2 

```sql 
CREATE EXTERNAL TABLE flight_delays_csv (
    yr INT,
    quarter INT,
    flightdate STRING,
    uniquecarrier STRING,
    ...

)
    PARTITIONED BY (year STRING)
    ROW FORMAT DELIMITED
      FIELDS TERMINATED BY ','
      ESCAPED BY '\\'
      LINES TERMINATED BY '\n'
    LOCATION 's3://athena-examples-myregion/flight/csv/';
```

## Method 3 

- http://www.devdailyhash.com/2017/09/aws-athena-to-query-csv-files-in-s3.html

```sql 
CREATE EXTERNAL TABLE IF NOT EXISTS athena_test.pet_data (
  `date_of_birth` string,
  `pet_type` string,
  `pet_name` string,
  `weight` string,
  `age` string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'quoteChar' = '"',
  'field.delim' = ','
) LOCATION 's3://test-athena-linh/pet/'
TBLPROPERTIES ('has_encrypted_data'='false');
```