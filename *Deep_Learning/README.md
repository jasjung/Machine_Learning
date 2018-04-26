# Deep Learning 

## Installation 

### TensorFlow 
https://www.tensorflow.org/install/install_mac

```
sudo easy_install --upgrade pip
sudo easy_install --upgrade six

pip3 install tensorflow
# pip3 uninstall tensorflow 

## Testing 
# python
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
```

### Keras 
https://keras.io

```
sudo pip install keras
```