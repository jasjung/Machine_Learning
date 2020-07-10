import java.io.*;
import java.util.*;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;
import org.apache.hadoop.mapred.lib.*;

/**
Data: s3://msiahw2/music/

Description: The data set is the same as in the previous exercise. For each artist in the data set, 
compute the maximum duration across all of his/her songs. The output should be: artist, max duration.

In addition, the management of your firm wants the artists’ names to be sorted across all files based 
on the first character. This means that the each output file of your MapReduce job must be sorted by the 
first character of an artist’s name. You cannot take the output files and then sort them in a spreadsheet
software. You are only allowed to concatenate the output files in the end.

In order to save computing resources for your firm, you have to use 5 reducers.

>> ARTIST, MAX DURATION

*/

public class Exercise4 extends Configured implements Tool {
	public static class Map extends MapReduceBase implements Mapper<LongWritable, Text, Text, DoubleWritable> {
		public void map(LongWritable key, Text inputLine, OutputCollector<Text, DoubleWritable> output, Reporter reporter) throws IOException {
			
	    	String[] line = inputLine.toString().split(",");  
			String artist = line[2]; // col3 = artist name
			double duration = Double.parseDouble(line[3]); // col4 = duration 
			output.collect(new Text(artist), new DoubleWritable(duration));

		} // end of Map function 
	} // end of Map class 

	/** 
	PARTITIONER 

	I am only considering lowercase alphabets and divided them in the following manner: 
		abcde fghij klmno pqrst uvwxyz

	*/
	public static class Partition extends MapReduceBase implements Partitioner<Text, DoubleWritable> {
		public int getPartition(Text key, DoubleWritable value, int numReduceTasks) {    		

			String firstChar = key.toString().substring(0,1).toLowerCase();

			if(firstChar.compareTo("f")<0){
				return 0;
			}
			else if(firstChar.compareTo("k")<0) {
				return 1;
			} 
			else if (firstChar.compareTo("p")<0) {
				return 2;
			} 
			else if (firstChar.compareTo("u")<0) {
				return 3;
			} else {
				return 4;
			}
		}
	}

	/**
	REDUCER
	*/
	public static class Reduce extends MapReduceBase implements Reducer<Text, DoubleWritable, Text, DoubleWritable> {
		public void reduce(Text key, Iterator<DoubleWritable> values, OutputCollector<Text, DoubleWritable> output, Reporter reporter) throws IOException {
			
			double max = Double.MIN_VALUE; // or arbitrarily set it to something small
			
			while(values.hasNext()) {
				double next = values.next().get();
				if(next > max) {
					max = next;
				}    
			}
			output.collect(key, new DoubleWritable(max));
		} // end of reduce method 
	} // end of Reduce class 
	
	public int run(String[] args) throws Exception{
		JobConf conf = new JobConf(getConf(), Exercise4.class);
		conf.setJobName("hw2-ex4");

	    conf.setNumReduceTasks(5);

	    // output key-value 
		conf.setOutputKeyClass(Text.class);
		conf.setOutputValueClass(DoubleWritable.class);

		//map -> combine -> partition -> reduce 
		conf.setMapperClass(Map.class);	
		conf.setCombinerClass(Reduce.class); 
		conf.setPartitionerClass(Partition.class);
		conf.setReducerClass(Reduce.class);

		//input output format
		conf.setInputFormat(TextInputFormat.class);
		conf.setOutputFormat(TextOutputFormat.class);

		conf.set("mapreduce.output.textoutputformat.separator", ",");

		FileInputFormat.setInputPaths(conf, new Path(args[0]));
		FileOutputFormat.setOutputPath(conf, new Path(args[1]));

		JobClient.runJob(conf);
		return 0;
	}	

	public static void main(String[] args) throws Exception{
		int res = ToolRunner.run(new Configuration(), new Exercise4(), args);
		System.exit(res);
	}
} 