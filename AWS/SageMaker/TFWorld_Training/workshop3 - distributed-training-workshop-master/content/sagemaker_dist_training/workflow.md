---
title: "Workflow"
date: 2019-10-28T12:59:15-07:00
weight: 1
---
Navigate to
***distributed-training-workshop > notebooks > part-2-sagemaker***
You should see the following files:

```bash
part-2-sagemaker/
├── cifar10-sagemaker-distributed.ipynb
└── code
    ├── cifar10-multi-gpu-horovod-sagemaker.py
    └── model_def.py
```

|Files/directories|Description|
|-----|-----|
|cifar10-sagemaker-distributed.ipynb |This jupyter notebook contains code to define and kick off a SageMaker training job|
|code |This directory contains the training scrip and other training script dependencies|

![sagemaker_workflow](/images/sagemaker/workflow.png)

SageMaker is a fully-managed service, which means when you kick off a training job using the SageMaker SDK in the `cifar10-sagemaker-distributed.ipynb` notebook, few different things happen behind the scene

* SageMaker spins up request number of instances in a fully-managed SageMaker cluster
* SageMaker pulls the latest (or specified version) of TensorFlow container images, instantiates it on the new instances and loads the content of the `code` directory into the container
* SageMaker runs the training script on each instance. Since we're running distributed training SageMaker launches an `MPI` job with the right settings so that workers can communicate with each other.
* SageMaker copies the dataset over from Amazon S3 and makes it available inside the container for Training
* SageMaker monitors the training and updates progress on the Amazon SageMaker console
* SageMaker copies all the code and model artifacts to Amazon S3 after the training is finished

In addition, SageMaker does a lot more to ensure that the jobs run optimally and you get the best perfomance out-of-the box. As a user you don't have to worry about managing machine learning infrastructure.
