# How to deploy fasttext model into sagemaker 

- https://aws.amazon.com/blogs/machine-learning/enhanced-text-classification-and-word-vectors-using-amazon-sagemaker-blazingtext/

Download fasttext model 

```sh 
wget https://dl.fbaipublicfiles.com/fasttext/vectors-english/crawl-300d-2M-subword.zip

unzip crawl-300d-2M-subword.zip
```

Sagemaker deployment 

```py 
# convert the bin file to tar 
import tarfile
with tarfile.open('model-fasttext.tar.gz', mode='w:gz') as archive:
    archive.add('sld_tld_model/crawl-300d-2M-subword.bin', recursive=True)

# save the model in s3 
import sagemaker
sagemaker_session = sagemaker.Session()
inputs_fasttext = sagemaker_session.upload_data(path='model-fasttext.tar.gz', key_prefix='model')

# create sagemaker model 
import boto3
import json
region_name = boto3.Session().region_name
container = sagemaker.amazon.amazon_estimator.get_image_uri(region_name, "blazingtext", "latest")
role = sagemaker.get_execution_role()
sess = sagemaker.Session()
model_fasttext = sagemaker.Model(model_data = inputs_fasttext, 
                     image=container, # BlazingText docker image
                     role=role,
                     sagemaker_session=sess)
# choose an instance that has enough memory (e.g. 16gb)
instance = 'ml.m5.xlarge' 
model_fasttext.deploy(initial_instance_count=1, instance_type=instance) 
predictor_fasttext = sagemaker.RealTimePredictor(
				   endpoint=model_fasttext.endpoint_name, 
                   sagemaker_session=sess,
                   serializer=json.dumps,
                   deserializer=sagemaker.predictor.json_deserializer
                   )

# test out the endpoint
predictor_fasttext=sagemaker.tensorflow.model.TensorFlowPredictor(predictor_fasttext.endpoint, sagemaker_session)

word='hi'
payload = {"instances" : word}
result = predictor_fasttext.predict(payload)

# len(result[0]['vector']) # 300 
```