# SageMaker Notebook Instance


## when kernel keeps restarting 

try running the following command which restarts entire the jupyter notebook environtment. 

https://stackoverflow.com/questions/55580232/update-sagemaker-jupyterlab-environment

```sh 
sudo initctl restart jupyter-server --no-wait
```

