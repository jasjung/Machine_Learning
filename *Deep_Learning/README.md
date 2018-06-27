# Deep Learning 

## Installation 

### TensorFlow 
https://www.tensorflow.org/install/install_mac

```
sudo easy_install --upgrade pip
sudo easy_install --upgrade six

pip3 install tensorflow
# pip3 uninstall tensorflow 

pip3 install tensorflow-gpu
```

```py
## Testing 
# python
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
```
Because I am using Jupyter Notebook installed from Anaconda, I had to `conda install -c conda-forge tensorflow` to update tensorflow. I am still experimenting and learning how to set it up properly. 

### Keras 
https://keras.io

```
sudo pip install keras
```


### Keras Model Saving 
[Reference](https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model)

```
sudo pip install h5py
```

```py
from keras.models import load_model

model.save('my_model.h5')  # creates a HDF5 file 'my_model.h5'
del model  # deletes the existing model

# returns a compiled model
# identical to the previous one
model = load_model('my_model.h5')
```

## GPU or CPU Check 
Run either codes below to see if your Keras or Tensorflow is running GPU.  

```
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
```

```
from keras import backend as K
K.tensorflow_backend._get_available_gpus()
```