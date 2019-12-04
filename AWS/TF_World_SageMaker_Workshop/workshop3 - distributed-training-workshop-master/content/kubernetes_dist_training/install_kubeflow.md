---
title: "Install Kubeflow"
date: 2019-10-28T15:42:44-07:00
weight: 5
---

#### Download the kfctl CLI tool

```
curl --silent --location https://github.com/kubeflow/kubeflow/releases/download/v0.7.0-rc.6/kfctl_v0.7.0-rc.5-7-gc66ebff3_linux.tar.gz | tar xz

sudo mv kfctl /usr/local/bin
```

#### Get the latest Kubeflow configuration file

```
export CONFIG='https://raw.githubusercontent.com/kubeflow/manifests/v0.7-branch/kfdef/kfctl_aws.0.7.0.yaml'
```

#### Create environment and local variables

```
CLUSTER_NAME=$(eksctl get cluster --output=json | jq '.[0].name' --raw-output)
INSTANCE_ROLE_NAME=$(eksctl get iamidentitymapping --name ${CLUSTER_NAME} --output=json | jq '.[0].rolearn' --raw-output | sed -e 's/.*\///')
```
```
export BUCKET_NAME=tfworld2019
export KF_NAME=${CLUSTER_NAME}
export KF_DIR=$PWD/${KF_NAME}
```

#### Build your configuration files
We'll edit the configuration with the right names for the cluster and node groups before deploying Kubeflow.

```
mkdir -p ${KF_DIR}
cd ${KF_DIR}
kfctl build -V -f ${CONFIG}
export CONFIG_FILE=${KF_DIR}/kfctl_aws.0.7.0.yaml

```

#### Edit the configuration file to include the correct instance role name and cluster name
```
sed -i "s@eksctl-kubeflow-aws-nodegroup-ng-a2-NodeInstanceRole-xxxxxxx@$INSTANCE_ROLE_NAME@" ${CONFIG_FILE}
sed -i "s@kubeflow-aws@$CLUSTER_NAME@" ${CONFIG_FILE}
```

#### Apply the changes and deploy Kubeflow
```
cd ${KF_DIR}
rm -rf kustomize/
kfctl apply -V -f ${CONFIG_FILE}
```

#### Wait for resource to become available

Monitor changes by running kubectl get all namespaces command.
```
kubectl -n kubeflow get all
```
