# AWS EC2 

## SSH 

SSH into your EC2 instance 

```sh 
chmod 400 your-key.pem
ssh -i "your-key.pem" ubuntu@<your-ip>
```

## Ubuntu Setup

```sh
sudo apt update
sudo apt install python3-pip
```

### install AWS CLI 

- https://linuxconfig.org/install-aws-cli-on-ubuntu-18-04-bionic-beaver-linux 

```sh 
sudo apt install awscli
aws --version
```

