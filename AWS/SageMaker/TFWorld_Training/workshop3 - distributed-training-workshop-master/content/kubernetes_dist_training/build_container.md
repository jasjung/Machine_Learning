---
title: "Build training container image and push it to ECR"
date: 2019-10-28T16:51:02-07:00
weight: 7
---

#### Build a custom docker image with our training code

In our Dockerfile we start with an AWS Deep Learning TensorFlow container and copy our training code into the container.

```
cd ~/SageMaker/distributed-training-workshop/notebooks/part-3-kubernetes/
cat Dockerfile.gpu
```
Dockerfile.gpu Output:
```
FROM 763104351884.dkr.ecr.us-west-2.amazonaws.com/tensorflow-training:1.14.0-gpu-py36-cu100-ubuntu16.04
COPY code /opt/training/
WORKDIR /opt/training
```

#### Create a new Elastic Container Registry repository

* Navigate to [ECR and create a new repository](https://console.aws.amazon.com/ecr/home)
* Click create repository
* Provide a repository name
* Click create again
* Click **View push commands**
* Keep this open, we'll come back to this soon
![create repo](/images/eks/create_repo.png)
![push commands](/images/eks/push_commands.png)
#### Create a new Elastic Container Registry repository

* Head over to the terminal on JupyterLab and log-in to the AWS Deep Learning registry
```
$(aws ecr get-login --no-include-email --region us-west-2 --registry-ids 763104351884)
```
* Open the push instructions and run **Step 2**
 * Make sure to add `-f Dockerfile.cpu` or `-f Dockerfile.gpu` before the dot to specify CPU or GPU container:
  * `docker build -t tfworld2019 -f Dockerfile.cpu .`
  * `docker build -t tfworld2019 -f Dockerfile.gpu .`
* Run **Step 3**
* After that run **Step 1** and **Step 4**

{{% notice tip %}}
The reason for the non-linear order is that, you need to first log into the AWS Deep Learning container registry in order to build our container. Once the container is built, you then need to log into your own registry, so that you can push the container (Step 4)
{{% /notice %}}
