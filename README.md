# GitHub FLASK

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
