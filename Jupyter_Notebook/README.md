#Jupyter Notebook 

To make your jupyter notebook open web brower 
automatically, run these commands on the command line. 

```
# list all files 
- ls -a 
# edit this file 
- vi .bash_profile
# add this line and save
- export BROWSER=open
``` 
Now you should be good to go. 

reference: https://medium.com/@GalarnykMichael/install-spark-on-mac-pyspark-453f395f240b

## Random
If your notebook gives you error "IOPub data rate exceeded", try: 
`jupyter notebook --NotebookApp.iopub_data_rate_limit=1.0e10`