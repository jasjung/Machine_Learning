# Docker 

Reference 

- https://medium.com/@charlie.b.ohara/building-a-flask-rest-api-with-docker-94ca4219f460
- https://youtu.be/pGYAg7TMmp0
- install: https://www.youtube.com/watch?v=lNkVxDSRo7M
- https://medium.com/@nadaa.taiyab/how-to-dockerize-your-flask-app-and-deploy-to-aws-elastic-beanstalk-9f761b7f3dba -> this is good. 
- https://docs.docker.com/get-started/part2/
- General Tutorial: https://www.youtube.com/watch?v=YFl2mCHdv24

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

Running 

```
sudo docker run -p 5000:5000 <your docker img> 
-> go to localhost:5000

sudo docker run -p 80:5000 <your docker img> 
-> go to localhost since 80 is default port
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


## Dockerfile Example 

This was built for hosting a flask api app. 

```
FROM python:3.6-slim
MAINTAINER Jason Jung 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8888
ENTRYPOINT [ "python" ]
CMD ["server.py"]
```

## Docker Compose 

reference: 

- [https://docs.docker.com/compose/overview/](https://docs.docker.com/compose/overview/)


## Prune 

https://docs.docker.com/config/pruning/#prune-containers

```
# when you get not enough space error 
docker system prune -a

# other pruning commands 
docker image prune
docker system prune
```

### Docker Load Fail 

https://stackoverflow.com/questions/47977699/add-failed-no-such-file-directory-while-building-docker-image
