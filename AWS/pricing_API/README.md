# AWS PRICING API 

Reference: 

- https://aws.amazon.com/blogs/aws/aws-price-list-api-update-new-query-and-metadata-functions/
- https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/{offer_code}/current/index.{format}
- https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonSageMaker/current/index.json
- https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonSageMaker/current/index.csv

```py 
with open('info/aws_sagemaker_pricing.json') as f:
    price = json.load(f)
```
