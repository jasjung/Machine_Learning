import java.io.*;
import java.util.*;
import java.lang.reflect.Array;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;
import org.apache.hadoop.mapred.lib.*;

/**
Data: s3://msiahw2/music/
Description: The data for this problem is a subset of the million song database 
(https://www.kaggle.com/c/msdchallenge#description), and its size is 42GB. 
The file is in csv format. Your task is to extract the song title (column 2), 
artist’s name (column 3) and duration (column 4) for all songs published between the years 2000 and 2010. 
The year is in column 165 – note that some year entries can be erroneous, and should be discarded. 
You should do this as efficiently as possible in MapReduce.

*/

public class Exercise3 extends Configured implements Tool {
	public static class Map extends MapReduceBase implements Mapper<LongWritable, Text, Text, NullWritable> {

		public void configure(JobConf job) {}

		public void map(LongWritable key, Text inputLine, OutputCollector<Text, NullWritable> output, Reporter reporter) throws IOException {
			
	    	String[] line = inputLine.toString().split(",");  

			String year = line[165]; // col166 = year
			
			try{ // check if the year is valid 
				Integer yearInt = Integer.parseInt(year); 

				if (yearInt >= 2000 && yearInt <= 2010){ //for all songs published between the years 2000 and 2010. 

					String title = line[1]; // col2 = song title 
					String artist = line[2]; // col3 = artist name
					String duration = line[3]; // col4 = duration

					output.collect(new Text(title+", "+artist+", "+duration), NullWritable.get());
				}
			} // end of try 
			catch(NumberFormatException ex){
				// do nothing 
			} // end of catch 

		} // end of Map function 
	} // end of Map class 

	public static class Reduce extends MapReduceBase implements Reducer<Text, NullWritable, Text, NullWritable> {
		public void reduce(Text key, Iterator<NullWritable> values, OutputCollector<Text, NullWritable> output, Reporter reporter) throws IOException {
			
			output.collect(key, NullWritable.get());

		}
	}

	public int run(String[] args) throws Exception{
		JobConf conf = new JobConf(getConf(), Exercise3.class);
		conf.setJobName("hw2-ex3");

		//conf.setMapOutputKeyClass(Text.class);
		//conf.setMapOutputValueClass(Text.class);
		
		conf.setOutputKeyClass(Text.class);
		conf.setOutputValueClass(NullWritable.class);

		conf.setMapperClass(Map.class);	
		conf.setCombinerClass(Reduce.class);
		conf.setReducerClass(Reduce.class);

	    //conf.setNumReduceTasks(1);

		conf.setInputFormat(TextInputFormat.class);
		conf.setOutputFormat(TextOutputFormat.class);
		conf.set("mapreduce.output.textoutputformat.separator", ",");

		FileInputFormat.setInputPaths(conf, new Path(args[0]));
		FileOutputFormat.setOutputPath(conf, new Path(args[1]));

		JobClient.runJob(conf);
		return 0;
	}	

	public static void main(String[] args) throws Exception{
		int res = ToolRunner.run(new Configuration(), new Exercise3(), args);
		System.exit(res);
	}
} 