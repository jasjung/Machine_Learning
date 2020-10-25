# Invoking sagemaker endpoint from lambda

- https://aws.amazon.com/blogs/machine-learning/call-an-amazon-sagemaker-model-endpoint-using-amazon-api-gateway-and-aws-lambda/
- https://stackoverflow.com/questions/57544237/inside-lambda-function-blazing-text-algorithm-invoke-endpoint-doesnt-support


## CALLING FASTTEXT 

```py
import json
import csv
import os
import io
import boto3

# grab environment variables
FASTTEXT_ENDPOINT = os.environ['FASTTEXT_ENDPOINT']

runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    
    data = json.loads(json.dumps(event))
   
    response = runtime.invoke_endpoint(EndpointName=FASTTEXT_ENDPOINT
                                      ,ContentType='application/json'
                                      ,Body=json.dumps(data)
                                      )
    
    t = json.loads(response['Body'].read().decode('utf-8'))
    embedding = t[0]['vector']

    return -1 # 
```
