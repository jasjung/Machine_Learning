---
title: "Install CLI tools"
date: 2019-10-28T15:02:28-07:00
weight: 2
---

#### Install `eksctl`

To get started we'll fist install the eksctl CLI tool. [eksctl](https://eksctl.io) simplifies the process of creating EKS clusters.

```bash
pip install awscli --upgrade --user
curl --silent --location "https://github.com/weaveworks/eksctl/releases/download/latest_release/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp

```

Move eksctl to /usr/local/bin to that it's on path

```
sudo mv /tmp/eksctl /usr/local/bin
eksctl version

```

#### Install `kubectl`
Kubectl is a command line interface for running commands against Kubernetes clusters. Run the following to install Kubectl

```bash
curl -o kubectl https://amazon-eks.s3-us-west-2.amazonaws.com/1.14.6/2019-08-22/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin
kubectl version --short --client

```

#### Install `aws-iam-authenticator`

```
curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.14.6/2019-08-22/bin/linux/amd64/aws-iam-authenticator

chmod +x ./aws-iam-authenticator

sudo mv aws-iam-authenticator /usr/local/bin
```
