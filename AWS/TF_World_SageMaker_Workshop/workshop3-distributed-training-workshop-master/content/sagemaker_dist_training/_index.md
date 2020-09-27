+++
title = "Distributed Training with Amazon Sagemaker"
date = 2019-10-21T13:21:01-07:00
weight = 4
chapter = true
# pre = "<b>1. </b>"
+++

# Distributed training with Amazon SageMaker

In this section, we'll run distributed training on Amazon SageMaker. We'll provide SageMaker with our updated training script that includes horovod API, and SageMaker will take care of the rest - spinning up requested number of CPU or GPU instances, copying the training code and dependencies to the training cluster, copying the dataset from Amazon S3 to the training cluster, keeping track of training progress and shutting down the instances once training is done. Amazon SageMaker is a fully managed service, so you don't have to worry about managing instances.
