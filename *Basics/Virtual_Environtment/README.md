# Virtual Environment

Reference 

- [https://www.youtube.com/watch?v=N5vscPTWKOk](https://www.youtube.com/watch?v=N5vscPTWKOk)
- https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe

current verdict: virtualenv > venv

## Virtualenv 

```
pip install virtualenv

# to view the list of pip packages 
pip list 
```

### Setting up your venv
```
mkdir virtualenv_tutorial
cd !$

# create virtual evn 
virtualenv project1_env

# activate 
source project1_env/bin/activate

# install packages 
pip install numpy # etc etc.. 

# to get the list of packages in the venv
# choose only the local dependencies 
pip freeze --local > requirements.txt

# to view 
cat requirements.txt

# to get out of the venv 
deactivate 

# to get rid of your venv project1_env
rm -rf project1_env
```

### Stage 2 

```
# create venv with specific python env (py27)
virtualenv -p /usr/bin/python2.7 py_env

# activate 
source py_env/bin/activate

python --version
# Python 2.7.10

# install packages from requirements.txt
pip install -r requirements.txt

# view 
pip list
```

## Venv (2019-06-07 Update)

Since Python 3.3, a subset of virtualenv has been integrated in the Python standard library under the venv module. For Python >= 3.3, you can create a virtual environment with:

```py 
python -m venv myvenv
```
