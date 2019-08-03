# aws sync 

https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html

### From EC2 Instance to S3 

```
aws s3 sync . s3://mybucket --exclude "*.jpg" 
```

### From S3 to Local 

```
aws s3 sync s3://mybucket . --exclude "*.jpg" 
```

## --dryrun

Use this argument to see which ones will upload without actually running. 


## Full Example 

syncing from sagemaker instance to s3 

```sh 
# dry run 
!aws s3 sync . s3://<your_bucket> --delete --exclude "*.lock" --exclude "*.bin" --exclude "node_modules/*" --exclude "lost+found" --exclude ".*" --exclude "*.pyc" --dryrun

# real run 
!aws s3 sync . s3://<your_bucket> --delete --exclude "*.lock" --exclude "*.bin" --exclude "node_modules/*" --exclude "lost+found" --exclude ".*" --exclude "*.pyc" 
```