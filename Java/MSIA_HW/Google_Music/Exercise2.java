import java.io.*;
import java.util.*;
import java.lang.reflect.Array;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;
import org.apache.hadoop.mapred.lib.*;

public class Exercise2 extends Configured implements Tool {

	/**
	Mapper 
	*/

	public static class Map1 extends MapReduceBase implements Mapper<LongWritable, Text, Text, Text> {

		//private DoubleWritable numVols = new DoubleWritable(); 

		private final Text dummyKey = new Text(" ");

		public void configure(JobConf job) {}

		public void map(LongWritable key, Text inputLine, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {
			
	    	String[] line = inputLine.toString().split("\\s+"); 

	    	String year = line[1];
	    	String volume = line[3]; 

			output.collect(dummyKey,new Text(volume));
		}		
	}	

	public static class Map2 extends MapReduceBase implements Mapper<LongWritable, Text, Text, Text> {
		
		private final Text dummyKey = new Text(" ");

		public void configure(JobConf job) {}

		public void map(LongWritable key, Text inputLine, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {
	    
	    	String[] line = inputLine.toString().split("\\s+"); 

	    	String year = line[2];
			String volume = line[4]; 

			output.collect(dummyKey,new Text(volume));
		}
	}	

	/**
	Combiner 
	*/
	public static class Combine extends MapReduceBase implements Reducer<Text, Text, Text, Text> {

		public void reduce(Text key, Iterator<Text> values, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {
		  
		  double count=0, sum=0, sumSqr=0;
		  
		  while(values.hasNext()){
		  		double num = Double.parseDouble(values.next().toString());
				sum += num;
				sumSqr += num*num; // Math.pow(num, 2); 
				count++;
			}
		  output.collect(key, new Text(String.valueOf(count)+","+String.valueOf(sum)+","+String.valueOf(sumSqr))); // do I need to use String.valueOf()
	 	} // end of combine method 
	} // end of combine class 

	/**
	Reducer
	*/
	public static class Reduce extends MapReduceBase implements Reducer<Text, Text, Text, Text> {
		public void reduce(Text key, Iterator<Text> values, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {

		double count=0, sum=0, sumSqr=0, mean=0,sd=0;

		while(values.hasNext()){
			String[] arr = values.next().toString().split(",");
			count += Double.parseDouble(arr[0]); // add the values from Combiner together 
			sum += Double.parseDouble(arr[1]);
			sumSqr += Double.parseDouble(arr[2]);
		} 

		mean = sum/count;
		sd = Math.sqrt((sumSqr - count*mean*mean)/count);
		output.collect(key, new Text(String.valueOf(sd)));

		} // end of reduce method 
	} // end of reduce class 


	public int run(String[] args) throws Exception{
		JobConf conf = new JobConf(getConf(), Exercise2.class);
		conf.setJobName("HW2-EX2");

		conf.setOutputKeyClass(Text.class);
		conf.setOutputValueClass(Text.class);

		conf.setMapperClass(Map1.class);
		conf.setMapperClass(Map2.class);
		conf.setCombinerClass(Combine.class);
		conf.setReducerClass(Reduce.class);

		conf.setInputFormat(TextInputFormat.class);
		conf.setOutputFormat(TextOutputFormat.class);

		MultipleInputs.addInputPath(conf,new Path(args[0]+"/googlebooks-eng-all-1gram-20120701-n"),TextInputFormat.class,Map1.class);
		MultipleInputs.addInputPath(conf,new Path(args[0]+"/googlebooks-eng-all-2gram-20120701-6"),TextInputFormat.class,Map2.class);
		FileOutputFormat.setOutputPath(conf, new Path(args[1]));

		JobClient.runJob(conf);
		return 0;
	}	

	public static void main(String[] args) throws Exception{
		int res = ToolRunner.run(new Configuration(), new Exercise2(), args);
		System.exit(res);
	}
} 