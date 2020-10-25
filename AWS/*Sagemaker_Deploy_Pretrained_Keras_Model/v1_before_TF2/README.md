# Deploy Pretrained Keras Model to Sagemaker Endpoint V1

https://aws.amazon.com/blogs/machine-learning/deploy-trained-keras-or-tensorflow-models-using-amazon-sagemaker/

The following code was used for tensorflow versions < 2.0. Used early 2019. 

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
from tensorflow.python.saved_model import builder
from tensorflow.python.saved_model.signature_def_utils import predict_signature_def
from tensorflow.python.saved_model import tag_constants

# This directory structure will need to be followed 
model_version = '1'
export_dir = 'export/Servo/' + model_version

# Build the Protocol Buffer SavedModel at 'export_dir'
builder = builder.SavedModelBuilder(export_dir)

# Create prediction signature to be used by TensorFlow Serving Predict API
signature = predict_signature_def(
    inputs={"inputs": loaded_model.input}
    ,outputs={"score": loaded_model.output}
    )

from tensorflow.keras import backend as K

with K.get_session() as sess:
    # Save the meta graph and variables
    builder.add_meta_graph_and_variables(
        sess=sess, tags=[tag_constants.SERVING], signature_def_map={"serving_default": signature})
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

!touch train.py

from sagemaker.tensorflow.model import TensorFlowModel
sagemaker_model = TensorFlowModel(model_data = 's3://' + sagemaker_session.default_bucket() + '/model/model.tar.gz',
                                  role = role,
                                  entry_point = 'train.py',
                                 )

# deploy 
predictor = sagemaker_model.deploy(initial_instance_count=1,
                                   instance_type='ml.m4.xlarge')
endpoint_name = predictor.endpoint
# you can start predicting 
predictor.predict(your_data)

# to call or point to a deployed endpoint 
import sagemaker
from sagemaker.tensorflow.model import TensorFlowPredictor
predictor=TensorFlowPredictor(endpoint_name, sagemaker_session)


#############################################################
# invoke with boto3 
#############################################################
import json
import boto3
import numpy as np
import io
 
client = boto3.client('runtime.sagemaker')
# The sample model expects an input of shape [1,50]
data = np.random.randn(1, 50).tolist()
response = client.invoke_endpoint(EndpointName=endpoint_name, Body=json.dumps(data))
response_body = response['Body']
print(response_body.read())

```


To Delete Endpoints 

```py
import boto3
client = boto3.client('sagemaker')
...
```