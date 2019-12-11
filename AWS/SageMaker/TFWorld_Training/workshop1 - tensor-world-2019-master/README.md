### To start the workshop, create an Amazon SageMaker Notebook Instance.

An Amazon SageMaker notebook instance is a fully managed machine learning compute instance that runs Jupyter Notebook App. You can use the notebook instance to build, train and test machine learning models. 


**To create an Amazon SageMaker notebook instance**

1. Go to https://dashboard.eventengine.run

2. Enter the hash provided by the workshop administrator and click on Proceed

3. Click on AWS Console

4. Click on Open Console. This will launch AWS Console. Note - you can disregard the credential information

5. Navigate to "Amazon SageMaker" under Services
    
6. Choose **Notebook instances**, then choose **Create notebook instance**
    
7. On the **Create notebook instance** page, provide the following information (if a field is not mentioned below, leave it default):
    
    a. For **Notebook instance name**, enter a name for your notebook instance
        
    b. For **Instance type**, choose `ml.m5.xlarge`
        
    c. For **IAM role**, choose **Create a new role**, then choose **Create role**. In 'create IAM Role' pop up window, select 'Any S3 bucket' 
        
    d. For Git repositories, select 'clone public git repo ***' and provide following repository: ``https://github.com/rthamman/tensor-world-2019.git``
        
    e. Choose **Create notebook instance**. In a few minutes, Amazon SageMaker will launch a ML compute instance. The notebook instance will have a preconfigured Jupyter notebook server and a set of Anaconda libraries. 

8. In few minutes Amazon SageMaker Instance will be in running state. Click **Open Jupyter** to continue. This will open Jupyter Notebook in your browser window. 

9. In the Jupyter Notebook console, in the Files tab, you will see the following. Run through the notebooks cell by cell. Order in which you execute the notebooks doesn't matter but it is recommended to follow the notebooks as listed below.
    
   a. Lab 1 (sentiment-analysis.ipynb) - this notebook demonstrates the following features:
	- A simple Natural Language Processing (NLP) model
	- Local Mode Training
	- Hosted Training Mode
	- Batch Prediction

   b. Lab 2 (tf-boston-housing.ipynb) - this notebook demonstrates the following features:
	- A simple Regression model
	- Local Mode Training
	- Local Mode Endpoint
	- Hosted Training Mode with model extraction for running it elsewhere
	- Hosted Endpoint
	- Automatic Model Tuning

   c. Lab 3 (tf-distributed-training.ipynb) - this notebook demonstrates the following features:
	- Distributed Training using Parameter Servers
	- Distributed Training using Horovod
   
10. Choose the Ipython notebook and follow the instructions in Jupyter Notebook. 
