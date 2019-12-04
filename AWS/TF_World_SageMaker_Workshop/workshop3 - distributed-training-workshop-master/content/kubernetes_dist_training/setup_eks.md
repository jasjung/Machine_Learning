---
title: "Setup an Amazon EKS cluster"
date: 2019-10-28T15:14:12-07:00
weight: 3
---

Navigate to ***distributed-training-workshop > notebooks > part-3-sagemaker***

The `cpu_eks_cluster.sh` and `gpu_eks_cluster.sh` files include the necessary options to lauch a CPU or GPU cluster. Take a look at the options by running the following script to launch an EKS clusters

```bash
cat cpu_eks_cluster.sh
```
You should see the following output
```
Output:
eksctl create cluster \
    --name aws-tf-cluster-cpu \
    --version 1.14 \
    --region us-west-2 \
    --nodegroup-name cpu-nodes \
    --node-type c5.xlarge \
    --nodes 2 \
    --node-volume-size 50 \
    --node-zones us-west-2a \
    --timeout=40m \
    --zones=us-west-2a,us-west-2b,us-west-2c \
    --auto-kubeconfig
```

Update the `nodes` argument to increase the number of nodes you want in the cluster. Now launch an EKS cluster:
```
sh cpu_eks_cluster.sh
```

You should an output that something similar to this.

![eks output](/images/eks/eksctl_launch.png)

Creating a cluster may take about 15 mins. You could head over to [AWS cloud formation console](https://console.aws.amazon.com/cloudformation) to monitor the progress.
