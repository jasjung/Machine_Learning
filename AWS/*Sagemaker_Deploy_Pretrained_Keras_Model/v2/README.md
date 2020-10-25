# Deploy Pretrained Keras Model to Endpoint v2 

![tensorflow 1.15.2](https://img.shields.io/badge/tensorflow-1.15.2-orange.svg)
![tf-keras 2.2.4](https://img.shields.io/badge/tf_keras-2.2.4-red.svg)
![keras 2.3.1](https://img.shields.io/badge/keras-2.3.1-red.svg)
![sagemaker 1.72.1](https://img.shields.io/badge/sagemaker-1.72.1-red.svg)

*Developed late 2020.*

Some differences since V1: 

- Use `from sagemaker.tensorflow.serving import Model`
instead of `from sagemaker.tensorflow.model import TensorFlowModel`
- Used `conda_amazonei_tensorflow_p36` kernalinstead of `conda_tensorflow_p36` in sagemaker notebook. I had some unknown issues with deployment, but changing the kernal fixed it. 
- import for builder is a bit different: `from tensorflow.python.saved_model import builder as saved_model_builder` 


```py 
#############################################################
# LOAD PRETRAINED MOEDL AND PREPARE 
#############################################################
from tensorflow.keras.models import load_model
from sagemaker import get_execution_role
import boto3, re
import keras
from tensorflow.keras.models import model_from_json

role = get_execution_role()
model = load_model("your_model.h5")

# serialize model to JSON
model_json = model.to_json()
with open("your_model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("models/your_model_weight.h5")
print("Saved model to disk")

# LOAD JSON MODEL 
json_file = open("your_model.json", 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights('your_model_weight.h5')
print("Loaded model from disk")


#############################################################
# EXPORT KERAS TO TENSORFLOW PROTOBUF FORMAT 
#############################################################
from tensorflow.python.saved_model import builder as saved_model_builder
from tensorflow.python.saved_model.signature_def_utils import predict_signature_def
from tensorflow.python.saved_model import tag_constants
# from tensorflow.compat.v1.keras import backend as K
!rm -r export/

model_version = '1'
export_dir = 'export/Servo/' + model_version
# Build the Protocol Buffer SavedModel at 'export_dir'
builder = saved_model_builder.SavedModelBuilder(export_dir)
# Create prediction signature to be used by TensorFlow Serving Predict API
signature = predict_signature_def(
    inputs={"inputs": loaded_model.input}
    ,outputs={"score": loaded_model.output}
    )

from keras import backend as K
with K.get_session() as sess:
    # Save the meta graph and variables
    builder.add_meta_graph_and_variables(
        sess=sess
        ,tags=[tag_constants.SERVING]
        ,signature_def_map={"serving_default": signature}
        )
    builder.save()

# check files 
# should see sth like: variables.data-00000-of-00001  variables.index
!ls export/Servo/1/variables

#############################################################
# Prepare for sagemaker 
#############################################################
import tarfile
with tarfile.open('model.tar.gz', mode='w:gz') as archive:
    archive.add('export', recursive=True)

# upload the model to s3 
import sagemaker
sagemaker_session = sagemaker.Session()
inputs = sagemaker_session.upload_data(path='model.tar.gz', key_prefix='model')


#############################################################
# DEPLOY 
#############################################################
from sagemaker.tensorflow.serving import Model
from sagemaker import get_execution_role
from sagemaker.tensorflow.model import TensorFlowPredictor
role = get_execution_role()

sagemaker_model2 = Model(model_data = 's3://' + sagemaker_session.default_bucket() + '/model/model.tar.gz'
						,role = role
                       )

predictor2 = sagemaker_model2.deploy(initial_instance_count=1
                                   ,instance_type='ml.m5.large' 
                                  )
endpoint_name = predictor2.endpoint
print('endpoint_name:',endpoint_name)
# start predicting 
predictor2.predict(data)

# to call or point to a deployed endpoint 
predictor2_endpoint = TensorFlowPredictor(endpoint_name, sagemaker_session)
```


## INVOKE ENDPOINT USING BOTO3 

- This is necessary when you want to call endpoint from lambda as you have to be able to serialize the data. 
- The model here takes in word embedding to predict a class. 

```py
# convert word embedding into a string 
# your_word_embedding (single example of 300 dimension)
new_emb = ", ".join([str(i) for i in your_word_embedding])
response = client.invoke_endpoint(EndpointName=endpoint_name,
                                  ContentType='text/csv',
                                  Body = new_emb.encode('utf-8')
                                  )
result = json.loads(response['Body'].read().decode())
print(result)
```

