# Keras

## Save Keras into TF model 

```
from keras import backend as K
import tensorflow as tf
print(model.output.op.name)

saver = tf.train.Saver()
saver.save(K.get_session(), 'tf_model/keras_model.ckpt')
```