---
title: "Monitoring training progress"
date: 2019-10-28T13:54:27-07:00
weights: 4
---

### Monitoring training progress using tensorboard

The ***cifar10-sagemaker-distributed.ipynb*** notebook will automatically start a tensorboard server for you when your run the following cell. Tensorboard is running locally on your Jupyter notebook instance, but reading the events from the Amazon S3 bucket we used to save the events using the keras callback.

```bash
!S3_REGION=us-west-2 tensorboard --logdir s3://{bucket_name}/tensorboard_logs/
```

Navigate to https://tfworld2019.notebook.us-west-2.sagemaker.aws/proxy/6006/

Replace `tfworld2019` with the name of your Jupyter notebook instance.
![tensorboard](/images/sagemaker/tensorboard.png)

### Monitoring training job status on the AWS SageMaker console

Navigate to ***AWS management console > SageMaker console*** to see a full list of training jobs and their status.

![tensorboard](/images/sagemaker/aws_console.png)

To view cloudwatch logs from the training instances, click on the ***training job name > Monitor > View logs***
