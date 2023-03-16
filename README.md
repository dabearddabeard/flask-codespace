# GitHub FLASK

Install virtualenvwrapper using the following cmds:
```
pip3 install virtualenvwrapper
export WORKON_HOME-~/workspace
source /usr/local/bin/virtualenvwrapper.sh
```

create a virtualenv  and install Flask
```
mkvirtualenv my_flask_env
pip3 install flask
```

to deactivate a virtualenv 
```
deactivate
```

to activate an existing virtualenv using virtualenvwrapper, run the following cmd
```
workon my_flask_env
```

install the application along with all the dependencies mention in install_requires
```
python setup.py install
```

```
flask --debug run
```
