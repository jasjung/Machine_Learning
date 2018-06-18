# Oozie 

## Virtual Memory Issue
If you are get getting error message that **Container is running beyond virtual memory limits**, try changing the following parameter is oozie's workflow.xml. I never had a problem running my pyspark code except when I put it on oozie. I simplyed doubled `oozie.launcher.mapreduce.map.memory.mb` and on longer had the issue. 

```
<property>
	<name>oozie.launcher.mapreduce.map.memory.mb</name>
		<!--<value>8120</value>-->
      	<value>16240</value>
</property>
```

## References 

tutorial: https://www.edureka.co/blog/apache-oozie-tutorial/

