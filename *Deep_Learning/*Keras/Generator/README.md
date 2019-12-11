# Generator for CSV File 

Reference: 

- https://stanford.edu/~shervine/blog/keras-how-to-generate-data-on-the-fly
- https://medium.com/@mrgarg.rajat/training-on-large-datasets-that-dont-fit-in-memory-in-keras-60a974785d71
- https://www.pyimagesearch.com/2018/12/24/how-to-use-keras-fit-and-fit_generator-a-hands-on-tutorial/ -> this 
- https://keras.io/models/sequential/
- Example of solving when number of predictions is fewer than actual count: https://stackoverflow.com/questions/48551158/keras-predict-generator-not-returning-correct-number-of-samples

---- 

Goald: Using Custom Data Generator for CSV Dataset. 

## CSV Data, Not Image 

- `flow_from_dataframe`
- `ImageGenerator`
- `fit_generator` 

## Predict_Generator()

From Documentation: 

- `steps_per_epoch`: Integer. Total number of steps (batches of samples) to yield from generator before declaring one epoch finished and starting the next epoch. It should typically be equal to ceil(num_samples / batch_size) Optional for Sequence: if unspecified, will use the len(generator) as a number of steps. (https://keras.io/models/sequential/)

## Example

See `generator_example.py`. 

```py 
# fit 
model.fit_generator(
            trainGen,
            steps_per_epoch=np.ceil(NUM_TRAIN_SET/BatchSize),
            validation_data=valGen,
            validation_steps=np.ceil(NUM_VAL_SET/BatchSize),
            epochs=NUM_EPOCHS)

# predict 
model.predict_generator(testGen, 
            steps=np.ceil(NUM_TEST_SET/BatchSize))
```

Few assumptions/notes: 

1. Create separate CSV fields for train, validation, and test. 
2. Standardize and shuffle the data before loading into the modeling step. You can do this while loading the file, but my example assumes that standardization and shuffling is already completed. 
3. My code assumes there is a header in the CSV file. 
4. My code assumes the target variable is the first column of the file and is binary of 1 and 0. 
5. Dataset either has no categorical features or has already been featurized into numerical information. 

