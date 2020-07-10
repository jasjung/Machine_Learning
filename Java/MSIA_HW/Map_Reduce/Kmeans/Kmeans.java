/* Jason Jung */
/*
import java.io.*;
import java.util.*;
import java.lang.*; 

//import java.io.IOException;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;
import org.apache.hadoop.mapred.lib.*;
import org.apache.hadoop.filecache.DistributedCache;
*/

import java.io.*;
import java.util.*;
import java.lang.*;

import org.apache.hadoop.fs.*;  
import org.apache.hadoop.filecache.*;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;

//import java.util.Scanner;
import java.util.ArrayList;
//import java.io.FileNotFoundException;

public class Kmeans extends Configured implements Tool {

	public static class Map extends MapReduceBase implements Mapper<LongWritable, Text, Text, Text> {		
        
        List<ArrayList<Double>> centroids = new ArrayList<ArrayList<Double>>();  
        //int k = 0;

/**
CONFIGURE
*/
		public void configure(JobConf conf) {

				// to temporarily store list for each centroid
				ArrayList<Double> numberDouble = new ArrayList<Double>();

            try{

            	// Distributed Cache 
	           	Path[] localFiles=new Path[0];
	           	localFiles = DistributedCache.getLocalCacheFiles(conf);
	           	BufferedReader fileIn = new BufferedReader(new FileReader(localFiles[0].toString()));


				String eachLine = null;
	            while ((eachLine = fileIn.readLine()) != null) {
	                //eachLine = scan.nextLine();
	                StringTokenizer tokenizer = new StringTokenizer(eachLine);

	                while (tokenizer.hasMoreTokens()){ 
	                    String number = tokenizer.nextToken();
	                    numberDouble.add(Double.parseDouble(number));
	                } // end of second while 
	                                
	                centroids.add(new ArrayList<Double>(numberDouble));
	                numberDouble.clear();                
	            } // end of first while 
            } catch (Exception e) {
                System.err.println("Exception reading DistribtuedCache: " + e);
			} // end of catch 

			// number of the clusters 
			//k = centroids.size(); 
		} // end of configure 
 
/**
MAP
*/
		public void map(LongWritable key, Text inputLine, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {
			
			/*
				Read each line -> 60 numbers  eg. "3 3 5 2 3"
				tokenize them -> 3, 3, 5, 3
			*/

	    	//String[] line = inputLine.toString().split("\\s+");  
	    	//String word = line[0]; 

            String line = inputLine.toString();
			StringTokenizer tokenizer = new StringTokenizer(line);

            ArrayList<Double> inputDouble = new ArrayList<Double>(); // contains all numbers 

            // reading in each number out of 60 columns 
            while (tokenizer.hasMoreTokens()) {   
                inputDouble.add(Double.parseDouble(tokenizer.nextToken()));
            }
            // calculate distance between numberDouble and all centroids 

            double minDistance = Double.MAX_VALUE; 
            int assignCluster = 0;

            // loops through each centroid 
            for (int i = 0; i < centroids.size(); i++) {
            	//i = centroid number 
            	//j = column number 
				double sum = 0;
                for (int j = 0; j < inputDouble.size(); j++) {
                	// Calculate Eucledean distance 
                    sum += Math.pow((inputDouble.get(j) - centroids.get(i).get(j)),2); 
                } // end of j loop 

                double currentDist = 0;
                currentDist = Math.sqrt(sum); 
                if (currentDist < minDistance) {
                    assignCluster = i;//i+1;
                    minDistance = currentDist;
                }   
            } // end of i loop 

            output.collect(new Text(String.valueOf(assignCluster)), new Text(inputLine)); 
        } // end of map method   
    } // end of map class   

/**
REDUCE 
*/
	public static class Reduce extends MapReduceBase implements Reducer<Text, Text, Text, Text> {  
		public void reduce(Text key, Iterator<Text> values, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {
			
			//Goal: Recompute the centroid
			//key: clusted number (eg 1,2,3) 
			//input: all the inputlines that are in each cluster 
			//Sum by column

			ArrayList<Double> newCentroid = new ArrayList<Double>();
            String[] firstObs = values.next().toString().split("\\s+");
			int numberOfObs = 1; // number of observatiosn in the dataset. 

    		// initialzie newCentroid variable with the first observation 
			for (int i = 0; i < firstObs.length; i++) {
				newCentroid.add(Double.parseDouble(firstObs[i]));
			}

			// SUM up each column 
            while (values.hasNext()) {
            	// Start of second 
                String[] nextObs = values.next().toString().split("\\s+"); 
                for (int i = 0; i < nextObs.length; i++) {
                    double sum = newCentroid.get(i) + Double.parseDouble(nextObs[i]);
                    newCentroid.set(i,sum);
                }
                numberOfObs++;
            }

            // calculate MEAN  
            for (int i = 0; i < newCentroid.size(); i++) {
                double mean = newCentroid.get(i)/numberOfObs;
                newCentroid.set(i,mean);
            }

            // convert newCentroid into string 
			String outputValue = "";
            for (int i = 0; i < newCentroid.size(); i++) {
                //if (i == 0) outputValue = newCentroid.get(i).toString();
                //else  outputValue  = outputValue + " " + newCentroid.get(i).toString();
                outputValue = outputValue + newCentroid.get(i).toString() + " ";
            }
            output.collect(new Text(outputValue), new Text(" "));

            //output.collect(new Text(""), new Text(inputLine)); 
		} // end of reduce method 
	} // end of reduce class 

	public int run(String[] args) throws Exception{ 
		JobConf conf = new JobConf(getConf(), Kmeans.class); 
		conf.setJobName("Kmeans");

    	conf.setMapOutputKeyClass(Text.class);
    	conf.setMapOutputValueClass(Text.class);

		conf.setOutputKeyClass(Text.class);
		conf.setOutputValueClass(Text.class);

		conf.setMapperClass(Map.class);
		conf.setReducerClass(Reduce.class);

		conf.setInputFormat(TextInputFormat.class);
		conf.setOutputFormat(TextOutputFormat.class);
		//conf.set("mapreduce.output.textoutputformat.separator", ",");

        FileInputFormat.setInputPaths(conf, new Path(args[0]));		
        FileOutputFormat.setOutputPath(conf, new Path(args[1]));
        //DistributedCache.addCacheFile(new Path("/home/jjung/hw3/centroids.txt").toUri(),conf);
        DistributedCache.addCacheFile(new Path("hw3/centroid/centroids.txt").toUri(),conf);

		JobClient.runJob(conf);
		return 0;
	} // end of run 

	public static void main(String[] args) throws Exception{
		int res = ToolRunner.run(new Configuration(), new Kmeans(), args);
		System.exit(res);
	}
} 