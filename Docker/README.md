# Docker 

Reference 

- https://medium.com/@charlie.b.ohara/building-a-flask-rest-api-with-docker-94ca4219f460
- https://youtu.be/pGYAg7TMmp0
- install: https://www.youtube.com/watch?v=lNkVxDSRo7M
- https://medium.com/@nadaa.taiyab/how-to-dockerize-your-flask-app-and-deploy-to-aws-elastic-beanstalk-9f761b7f3dba -> this is good. 
- https://docs.docker.com/get-started/part2/

docker.com/toolbox -> download mac version 

to test

```sh 
docker run hello-world 
docker info 
docker --version
```

#### Saving and Loading Docker Img

[https://stackoverflow.com/questions/23935141/how-to-copy-docker-images-from-one-host-to-another-without-using-a-repository](https://stackoverflow.com/questions/23935141/how-to-copy-docker-images-from-one-host-to-another-without-using-a-repository)

```
docker save -o <path for generated tar file> <image name>
docker load -i <path to image tar file>
```


### Linux 

CentOS 

```
sudo yum install docker-io
sudo yum install python3-pip
```

```
RUN yum install -y python36u-pip && \
	yum install python36u && \
    pip install --upgrade pip
```