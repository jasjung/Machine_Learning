# How to Train on AWS GPU 

References: 

- [SagaMaker SDK](https://sagemaker.readthedocs.io/en/stable/index.html)
- [CLI User Setup](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)

## Install 

```
pip install awscli --upgrade --user
```
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html


## Configure 

```sh 
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-west-2
Default output format [None]: json
```

## AWS ML Training

References: 

- Offical Training: [aws.training/machinelearning](https://aws.amazon.com/training/learning-paths/machine-learning/)


## AWS DL AMI (Deep Learning Amazon Machine Image)

References: 

- DLAMI: [https://docs.aws.amazon.com/dlami/latest/devguide/what-is-dlami.html](https://docs.aws.amazon.com/dlami/latest/devguide/what-is-dlami.html)
- Getting started with DLAMI: [https://aws.amazon.com/getting-started/tutorials/get-started-dlami/](https://aws.amazon.com/getting-started/tutorials/get-started-dlami/) -> scroll down to see the instructions 
- How To by CS231n: [http://cs231n.github.io/aws-tutorial/](http://cs231n.github.io/aws-tutorial/)
- Tutorial: [https://towardsdatascience.com/boost-your-machine-learning-with-amazon-ec2-keras-and-gpu-acceleration-a43aed049a50](https://towardsdatascience.com/boost-your-machine-learning-with-amazon-ec2-keras-and-gpu-acceleration-a43aed049a50)
- Jupyter Notebook Setup:
	- [https://docs.aws.amazon.com/dlami/latest/devguide/setup-jupyter-configure-server.html](https://docs.aws.amazon.com/dlami/latest/devguide/setup-jupyter-configure-server.html)
	
 
Notes from the documentation: 

- If you're new to using AWS or using Amazon EC2, start with the [Deep Learning AMI with Conda.](https://docs.aws.amazon.com/dlami/latest/devguide/overview-conda.html)

```
```

### DL AMI 

Deep Learning AMI (Ubuntu) Version 17.0 - ami-047daf3f2b162fc35


### Sagemaker 

```
https://aws.amazon.com/sagemaker/pricing/
```

### Access Key ID and Secret Access Key 

credit: [https://supsystic.com/documentation/id-secret-access-key-amazon-s3/](https://supsystic.com/documentation/id-secret-access-key-amazon-s3/)

```
In order to get your Access Key ID and Secret Access Key follow next steps:

Open the IAM console.
From the navigation menu, click Users.
Select your IAM user name.
Click User Actions, and then click Manage Access Keys.
Click Create Access Key.
Your keys will look something like this:
Access key ID example: AKIAIOSFODNN7EXAMPLE
Secret access key example: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Click Download Credentials, and store the keys in a secure location.```


### Tags 

- https://cloudacademy.com/blog/what-are-best-practices-for-tagging-aws-resources/
- https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html
