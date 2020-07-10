# Word Count Example  

https://beam.apache.org/get-started/wordcount-example/

## MinimalWordCount example

MinimalWordCount demonstrates a simple pipeline that uses the Direct Runner to read from a text file, apply transforms to tokenize and count the words, and write the data to an output text file.


### 0. Init 

```sh 
# java 
$ mvn compile exec:java -Dexec.mainClass=org.apache.beam.examples.MinimalWordCount

# python
python -m apache_beam.examples.wordcount_minimal --input YOUR_INPUT_FILE --output counts
```

### 1. Creating the pipeline

```java 
// Create a PipelineOptions object. This object lets us set various execution
// options for our pipeline, such as the runner you wish to use. This example
// will run with the DirectRunner by default, based on the class path configured
// in its dependencies.
PipelineOptions options = PipelineOptionsFactory.create();

// create a Pipeline object with the options we’ve just constructed
Pipeline p = Pipeline.create(options);
```

```py 
options = PipelineOptions()
google_cloud_options = options.view_as(GoogleCloudOptions)
google_cloud_options.project = 'my-project-id'
google_cloud_options.job_name = 'myjob'
google_cloud_options.staging_location = 'gs://your-bucket-name-here/staging'
google_cloud_options.temp_location = 'gs://your-bucket-name-here/temp'
options.view_as(StandardOptions).runner = 'DataflowRunner'

# create a Pipeline object with the options we’ve just constructed
p = beam.Pipeline(options=options)
```

### 2. Applying pipeline transforms

```java 
// A text file Read transform is applied to the Pipeline object itself, and produces a PCollection as output. Each element in the output PCollection represents one line of text from the input file. This example uses input data stored in a publicly accessible Google Cloud Storage bucket (“gs://").
p.apply(TextIO.read().from("gs://apache-beam-samples/shakespeare/*"))

// This transform splits the lines in PCollection<String>, where each element is an individual word in Shakespeare’s collected texts
.apply("ExtractWords", FlatMapElements
    .into(TypeDescriptors.strings())
    .via((String line) -> Arrays.asList(line.split("[^\\p{L}]+"))))

// The SDK-provided Count transform is a generic transform that takes a PCollection of any type, and returns a PCollection of key/value pairs.
.apply(Count.<String>perElement())

// formats each of the key/value pairs of unique words and occurrence counts into a printable string suitable for writing to an output file.
.apply("FormatResults", MapElements
    .into(TypeDescriptors.strings())
    .via((KV<String, Long> wordCount) -> wordCount.getKey() + ": " + wordCount.getValue()))

// A text file write transform.
.apply(TextIO.write().to("wordcounts"));
```

```py 
p
| beam.io.ReadFromText('gs://dataflow-samples/shakespeare/kinglear.txt')
# The Flatmap transform is a simplified version of ParDo.
| 'ExtractWords' >> beam.FlatMap(lambda x: re.findall(r'[A-Za-z\']+', x))
| beam.combiners.Count.PerElement()
| beam.MapTuple(lambda word, count: '%s: %s' % (word, count))
| beam.io.WriteToText('gs://my-bucket/counts.txt')

```

### 3. Running the pipeline


```java 
p.run().waitUntilFinish();
```

```py 
result = p.run()
```
