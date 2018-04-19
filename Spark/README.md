# Spark 

## Installation

### Method 1 (Use Method 2)

To install Spark to your Mac: [Click Here](https://medium.com/@GalarnykMichael/install-spark-on-mac-pyspark-453f395f240b)

You'll have to install Java JDK beforehand:[Click Here](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

- Check if Java is installed on mac: `javac -version`

This method works. However, `findspark` function was not working as I wanted. Second method works as expected and is cleaner. 

### Method 2 

Reference: [Click Here](https://medium.freecodecamp.org/installing-scala-and-apache-spark-on-mac-os-837ae57d283f)

```
# install java 
brew cask install java

# install spark 
brew install scala
brew install apache-spark

# to test 
spark-shell

# in jupyternotebook
import findspark
findspark.find() 

from pyspark import SparkContext
sc =SparkContext()

sc.parallelize(range(1000)).count()
# out: 1000 

```

- https://stackoverflow.com/questions/34601554/mac-spark-shell-error-initializing-sparkcontext?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa


`sudo hostname -s 127.0.0.1`

## GraphFrame
Reference: [Click Here](https://databricks.com/blog/2016/03/03/introducing-graphframes.html)


