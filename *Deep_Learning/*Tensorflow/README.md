# Tensorflow

## Estimators 
- https://www.tensorflow.org/get_started/premade_estimators

## Embedding_Column
- https://www.tensorflow.org/programmers_guide/embedding 

```py
# given you have a dataframe and column called 'occupation'
categorical_column = tf.feature_column.categorical_column_with_vocabulary_list(key="occupation", vocabulary_list=df.occupation.unique())

number_of_categories= len(df.occupation.unique())
embedding_dimensions = math.ceil(number_of_categories**0.25)

embedded_col = tf.feature_column.embedding_column(categorical_column, embedding_dimensions)

# Then feed the embedded_col into DNNClassifier. 
```

References: 

- [Get Started](https://www.tensorflow.org/get_started/)
- [TFRecord](https://www.skcript.com/svr/why-every-tensorflow-developer-should-know-about-tfrecord/)
- https://medium.com/mostly-ai/tensorflow-records-what-they-are-and-how-to-use-them-c46bc4bbb564
- [TFServing](https://www.tensorflow.org/versions/r1.1/deploy/tfserve): TensorFlow Serving is a flexible, high-performance serving system for machine learning models, designed for production environments. TensorFlow Serving makes it easy to deploy new algorithms and experiments, while keeping the same server architecture and APIs.
- [feature_embedding](https://www.tensorflow.org/get_started/feature_columns#indicator_and_embedding_columns)
- https://codelabs.developers.google.com/codelabs/cloud-tensorflow-mnist/#0
- 