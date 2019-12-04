---
title: "Enable Amazon FSx for Lustre access"
date: 2019-10-28T16:20:52-07:00
weight: 6
---

Amazon FSx for Lustre provides a high-performance file system optimized for fast processing of workloads such as in deep learning. FSx for Lustre file system transparently presents S3 objects as files and allows you to write results back to S3.

#### Install the FSx CSI Driver
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-fsx-csi-driver/master/deploy/kubernetes/manifest.yaml
```


```
VPC_ID=$(aws ec2 describe-vpcs --filters "Name=tag:Name,Values=eksctl-${CLUSTER_NAME}-cluster/VPC" --query "Vpcs[0].VpcId" --output text)
```

#### Get subnet ID from the EC2 console
Navigate to [AWS EC2 console](https://console.aws.amazon.com/ec2/v2/home) and click on **Instances**.
Select one of the running instances which starts with the name of the EKS cluster. This instance is a node on the EKS cluster.
Copy the subnet ID as show in the image below. Click on the copy-to-clipboard icon show next to the arrow.

![subnet](/images/eks/subnet_image.png)
paste the subnet ID below
```
export SUBNET_ID=<subnet_id>
```

#### Create your security group for the FSx file system and add an ingress rule that opens up port 988 from the 192.168.0.0/16 CIDR range:
```
SECURITY_GROUP_ID=$(aws ec2 create-security-group --group-name eks-fsx-security-group --vpc-id ${VPC_ID} --description "FSx for Lustre Security Group" --query "GroupId" --output text)
export SECURITY_GROUP_ID=${SECURITY_GROUP_ID}

aws ec2 authorize-security-group-ingress --group-id ${SECURITY_GROUP_ID} --protocol tcp --port 988 --cidr 192.168.0.0/16
```

#### Update the environment variables in the storage class spec file
Running envsubst will populate SUBNET_ID, SECURITY_GROUP_ID, BUCKET_NAME
```
cd ~/SageMaker/distributed-training-workshop/notebooks/part-3-kubernetes/
envsubst < specs/storage-class-fsx-s3-template.yaml > specs/storage-class-fsx-s3.yaml
```

#### Deploy the StorageClass and PersistentVolumeClaim
```
kubectl apply -f specs/storage-class-fsx-s3.yaml
kubectl apply -f specs/claim-fsx-s3.yaml
```

This will take several minutes. You can check the status by running:

```
kubectl get pvc fsx-claim -w
```
