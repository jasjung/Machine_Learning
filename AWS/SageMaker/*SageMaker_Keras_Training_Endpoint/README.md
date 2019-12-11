# SageMaker Keras Training and Deploying

![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)
![Keras 2.2.4-tf](https://img.shields.io/badge/keras-2.2.4.tf-red.svg)
![tensorflow 1.14.0](https://img.shields.io/badge/tensorflow-1.14.0-orange.svg)
![sagemaker 1.14.0](https://img.shields.io/badge/sagemaker-1.45.0.dev0-green.svg)


Sadly, AWS documentation is all over the place and not very consistent. It is not often general enough. I had run into issues while I was trying to train and deploy a keras model. Following their documentation kept giving me errors. And, at last, I got it to work. 


### References 

- https://towardsdatascience.com/deploying-keras-models-using-tensorflow-serving-and-flask-508ba00f1037
- https://stackoverflow.com/questions/57172147/no-savedmodel-bundles-found-on-tensorflow-hub-model-deployment-to-aws-sagemak
- https://aws.amazon.com/blogs/machine-learning/deploy-trained-keras-or-tensorflow-models-using-amazon-sagemaker/


### Advice

- Even though sagemaker documentation uses following function to save model, it does not work when you for deplying (at least with the version I was using): `tf.contrib.saved_model.save_keras_model`. You want to use `tf.saved_model.simple_save()`. For details, refer to [this](https://towardsdatascience.com/deploying-keras-models-using-tensorflow-serving-and-flask-508ba00f1037) and [this](https://aws.amazon.com/blogs/machine-learning/deploy-trained-keras-or-tensorflow-models-using-amazon-sagemaker/).  
- Simply saving your model to `/opt/ml/model` is not good enough. You need something more like `/opt/ml/model/export/Servo/1`


### Various errors I ran into during my development 

- `raise ValueError('no SavedModel bundles found!')` 
- `Your model will NOT be servable with SageMaker TensorFlow Serving containers.The SavedModel bundle is under directory "model", not a numeric name.`
- `Could not find base path /opt/ml/model/export/Servo for servable generic_model`



