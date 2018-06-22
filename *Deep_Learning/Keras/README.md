# Keras

## Save Keras into TF model 

```py
from keras import backend as K
import tensorflow as tf
print(model.output.op.name)

saver = tf.train.Saver()
saver.save(K.get_session(), 'tf_model/keras_model.ckpt')
```

## Plot Loss/Accuracy

```py
# list all data in history
# summarize history for accuracy
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
```