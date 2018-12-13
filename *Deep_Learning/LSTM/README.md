# LSTM

Conceptual 

- http://colah.github.io/posts/2015-08-Understanding-LSTMs/

## In Keras 

https://faroit.github.io/keras-docs/1.2.1/layers/recurrent/

### Input_Shape 

LSTM has tricky input shape if you want this to be the first layer in your model 

Reference 

- [https://machinelearningmastery.com/reshape-input-data-long-short-term-memory-networks-keras/](https://machinelearningmastery.com/reshape-input-data-long-short-term-memory-networks-keras/)
- [https://machinelearningmastery.com/return-sequences-and-return-states-for-lstms-in-keras/](https://machinelearningmastery.com/return-sequences-and-return-states-for-lstms-in-keras/)


### return_sequences
Use `return_sequences=True` if you want to stack LSTM Layers 

### Categorical Y 

Reference: 

- [https://machinelearningmastery.com/multi-class-classification-tutorial-keras-deep-learning-library/](https://machinelearningmastery.com/multi-class-classification-tutorial-keras-deep-learning-library/)

If you are dealing with categorical classification problem, remember to one-hot-encode the y variable. 

### Loading Pretrained Word Embedding 

[https://machinelearningmastery.com/use-word-embedding-layers-deep-learning-keras/](https://machinelearningmastery.com/use-word-embedding-layers-deep-learning-keras/)