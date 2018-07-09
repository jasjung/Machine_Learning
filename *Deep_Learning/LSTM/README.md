# LSTM

## In Keras 

https://faroit.github.io/keras-docs/1.2.1/layers/recurrent/

### Input_Shape 

LSTM has tricky input shape if you want this to be the first layer in your model 

Reference 

- https://machinelearningmastery.com/reshape-input-data-long-short-term-memory-networks-keras/
- https://machinelearningmastery.com/return-sequences-and-return-states-for-lstms-in-keras/


### return_sequences
Use `return_sequences=True` if you want to stack LSTM Layers 

