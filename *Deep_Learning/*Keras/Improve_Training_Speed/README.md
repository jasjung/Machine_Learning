# Improve Training Speed 

https://medium.com/@joelognn/improving-cnn-training-times-in-keras-7405baa50e09

Use the following if you have GPU. 

```py 
history = model.fit_generator(
  ...,
  use_multiprocessing=True,
  workers=16
  )
```