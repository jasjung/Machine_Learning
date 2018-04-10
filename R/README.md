# R 

Tricks related to R 

## Apply Function 
- Reference: https://www.datacamp.com/community/tutorials/r-tutorial-apply-family#codesapplycode

```R 
# coming soon
```

## Train/Test Split 
```
# this was found online. Not my original code. 

# Set random seed. Don't remove this line.
set.seed(1)
# Shuffle the dataset, call the result shuffled 
n <- nrow(df_upsampled)
shuffled <- df_upsampled[sample(n),]

# Split the data in train and test
train <- shuffled[1:round(0.7 * n),]
test <- shuffled[(round(0.7 * n) + 1):n,]
```
## Logistic Regression 

## Spark R 
- https://spark.apache.org/docs/latest/sparkr.html

```R
if (nchar(Sys.getenv("SPARK_HOME")) < 1) {
  Sys.setenv(SPARK_HOME = "/home/spark")
}

library(SparkR, lib.loc = c(file.path(Sys.getenv("SPARK_HOME"), "R", "lib")))
sparkR.session(master = "local[*]", sparkConfig = list(spark.executor.memory = "4g",spark.driver.maxResultSize = "3g",spark.driver.memory = "8g"))
```

## Random Functions 
### Clean Column Name
```R 
clean_column = function(df)	{ unlist(lapply(strsplit(colnames(df),".",fixed=TRUE),`[`,2))
}

clean_column(your_df) 
```

### Check NAs
```R 
# check na 
check_na = function(df){
  temp = sapply(df,function(x) sum(is.na(x)))
  if (sum(temp)>0){
    # show just the cols with NAs 
    print('there are NAs')
    print(temp[temp>0])
    
  } else {
    print('there are no NAs')
  }
}
check_na(df)
```

### Pattern Matching 
```
# l = logical 
grepl('pattern', list_or_string)
```

### Complete Case / Is NA  
```R
# filter out rows with NAs 
df[complete.cases(df)]

# retrieve rows with NAs 
df[is.na(df)]
```

### Find Duplicate Rows 
- https://stackoverflow.com/questions/12495345/find-indices-of-duplicated-rows

```R
duplicated(df) | duplicated(df, fromLast = TRUE)
```