---
title: "Cleanup"
date: 2019-10-27T15:25:09-07:00
draft: true
weight: 6
---
In this section, we'll walkthrough steps to clean up resources.

## Amazon EKS resources

#### Kill all distributed training jobs
```
kubectl delete MPIJobs --all
```

#### Delete StorageClass, PersistentVolumeClaim and FSx for Lustre CSI Driver
{{% notice tip %}}
Note: This will automatically delete the FSx for luster file system. Your files are safe in Amazon S3.
{{% /notice %}}
```
kubectl delete -f specs/storage-class-fsx-s3.yaml
kubectl delete -f specs/claim-fsx-s3.yaml
kubectl delete -f https://raw.githubusercontent.com/kubernetes-sigs/aws-fsx-csi-driver/master/deploy/kubernetes/manifest.yaml
```
#### Delete security group
```
aws ec2 delete-security-group --group-id ${SECURITY_GROUP_ID}
```

#### Delete policies attached to the instance role
These policies were automatically added to the node IAM roles, but we'll need to manually remove them.
```
echo $INSTANCE_ROLE_NAME
```
* Navigate to IAM console
* Click on Roles on the left pane
* Search for the output of `echo $INSTANCE_ROLE_NAME`
* Delete the two inline policies.
 * `iam_alb_ingress_policy`
 * `iam_csi_fsx_policy`

#### Finally, delete the cluster
```
eksctl delete cluster aws-tf-cluster-cpu
```

## SageMaker resources
SageMaker resources are easier to clear.
Login into the SageMaker console and click dashboard
Make sure that you don't have any resources that are **Green** as shown below. Click on the resources that is shown as green and either stop or delete them.

![sm_dashboard](/images/cleanup/sm_cleanup.png)

## Other resources
It's always good idea to ensure that:

* Stop or terminate EC2 instances that's not currently in use, by navigating to the EC2 console
* Delete data stored on Amazon S3 that you don't need
