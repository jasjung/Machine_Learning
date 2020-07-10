import java.io.*;
import java.util.*;
import java.lang.*; 

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;
import org.apache.hadoop.mapred.lib.*;

public class Exercise1 extends Configured implements Tool {
	public static class Map1 extends MapReduceBase implements Mapper<LongWritable, Text, Text, Text> {		
		public void configure(JobConf job) {}

		public void map(LongWritable key, Text inputLine, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {
			
	    	String[] line = inputLine.toString().split("\\s+");  
	    	String word = line[0]; 
	    	String year = line[1]; 
	    	String volume = line[3];

		 	try{
		        Integer.parseInt(year); // check for erroneous interger 

				if(word.toLowerCase().contains("nu")) {
					output.collect(new Text(year + ", nu"), new Text(volume));
				}
				else if(word.toLowerCase().contains("chi")) {
					output.collect(new Text(year + ", chi"), new Text(volume));
				}
				else if(word.toLowerCase().contains("haw")) {
					output.collect(new Text(year + ", haw"), new Text(volume));
				}
			} // end of try 

			catch (NumberFormatException ex){ // do nothing 
			} // end of catch 
		}
	}	

	public static class Map2 extends MapReduceBase implements Mapper<LongWritable, Text, Text, Text> {
		public void map(LongWritable key, Text inputLine, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {

			String[] line = inputLine.toString().split("\\s+");  
			String word1 = line[0];
			String word2 = line[1];
	    	String year = line[2];
	    	String volume = line[4];

		 	try{
		        Integer.parseInt(year); // check for erroneous interger 

				if(word1.toLowerCase().contains("nu")) {
					output.collect(new Text(year + ", nu"), new Text(volume));
				}
				if(word2.toLowerCase().contains("nu")) {
					output.collect(new Text(year + ", nu"), new Text(volume));
				}
				if(word1.toLowerCase().contains("chi")) {
					output.collect(new Text(year + ", chi"), new Text(volume));
				}
				if(word2.toLowerCase().contains("chi")) {
					output.collect(new Text(year + ", chi"), new Text(volume));
				}
				if(word1.toLowerCase().contains("haw")) {
					output.collect(new Text(year + ", haw"), new Text(volume));
				}
				if(word2.toLowerCase().contains("haw")) {
					output.collect(new Text(year + ", haw"), new Text(volume));
				}
			} // end of try 

			catch (NumberFormatException ex){ // do nothing 
			} // end of catch 
		} // end of map function 
	}// end of map2 class 

/// COMBINER 
	public static class Combine extends MapReduceBase implements Reducer<Text, Text, Text, Text> {

		public void reduce(Text key, Iterator<Text> values, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {
		  
		  double count=0, sum=0;
		  
		  while(values.hasNext()){

				sum += Double.parseDouble(values.next().toString());
				count++;
			}

			/*
		  for (Text i:values){ // here the values = volume 
		  	sum += Double.parseDouble(i.toString());
		  	count++; 
		  }*/
		  output.collect(key,new Text(String.valueOf(count)+","+String.valueOf(sum)));
	 	}	

	} // end of combine class 

	public static class Reduce extends MapReduceBase implements Reducer<Text, Text, Text, Text> {
		public void reduce(Text key, Iterator<Text> values, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {

			double sum = 0;
			double count = 0; 

		  while(values.hasNext()){
		  		String[] value = values.next().toString().split(",");
		  		count += Double.parseDouble(value[0]); 
				sum += Double.parseDouble(value[1]); 
			}
/*
			for (Text i:values){
				String[] value = i.toString().split(",");  
				count += Double.parseDouble(value[0]); 
				sum += Double.parseDouble(value[1]); 
			}*/
			output.collect(key, new Text(String.valueOf(sum/count)));
		}
	}

	public int run(String[] args) throws Exception{
		JobConf conf = new JobConf(getConf(), Exercise1.class);
		conf.setJobName("hw2-ex1");

		conf.setOutputKeyClass(Text.class);
		conf.setOutputValueClass(Text.class);

		conf.setMapperClass(Map1.class);
		conf.setMapperClass(Map2.class);

		conf.setCombinerClass(Combine.class);
		conf.setReducerClass(Reduce.class);

		conf.setInputFormat(TextInputFormat.class);
		conf.setOutputFormat(TextOutputFormat.class);
		conf.set("mapreduce.output.textoutputformat.separator", ",");

		MultipleInputs.addInputPath(conf,new Path(args[0]+"/googlebooks-eng-all-1gram-20120701-n"),TextInputFormat.class,Map1.class);
		MultipleInputs.addInputPath(conf,new Path(args[0]+"/googlebooks-eng-all-2gram-20120701-6"),TextInputFormat.class,Map2.class);
		FileOutputFormat.setOutputPath(conf, new Path(args[1]));

		JobClient.runJob(conf);
		return 0;
	}	

	public static void main(String[] args) throws Exception{
		int res = ToolRunner.run(new Configuration(), new Exercise1(), args);
		System.exit(res);
	}
} 