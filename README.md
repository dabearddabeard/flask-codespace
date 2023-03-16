# FLASK for GitHub Codespaces
### GitHub Codespaces 
A cloud-based development environment for writing, debugging, testing and deploying code. It provides developers with on-demand access to a secure development environment running a given codebase (Git repository) on a remote server. The Codespaces development environment runs in a virtual machine in the cloud and can be customized for any development project on GitHub by pre-installing dependencies, libraries, and even Visual Studio Code extensions and settings.
### Flask 
A micro web framework written in Python. It provides libraries to build lightweight web applications in python.


## Codespace
Click

<img src="button.svg" alt="Button" width="200" height="50">



On the Codespaces tab, click

<img src="button1.svg" alt="Button" width="200" height="50">



## Clone to your local machine instead of using Codespace: 
Navigate to the directory where you want to clone
```
git clone https://github.com/dabearddabeard/flask-codespace.git
```


Install virtualenvwrapper using the following cmds:
```
pip3 install virtualenvwrapper
export WORKON_HOME-~/workspace
source /usr/local/bin/virtualenvwrapper.sh
```


Create a virtualenv and install Flask
```
mkvirtualenv my_flask_env
pip3 install flask
```


Deactivate a virtualenv 
```
deactivate
```


Activate an existing virtualenv using virtualenvwrapper, run the following cmd
```
workon my_flask_env
```


Install the application along with all the dependencies mention in install_requires
```
python setup.py install
```


Run
```
python run.py
```
