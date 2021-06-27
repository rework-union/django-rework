# Django Rework

[![Downloads](https://pepy.tech/badge/django-rework)](https://pepy.tech/project/django-rework)
[![PyPI](https://img.shields.io/pypi/v/django-rework)](https://pypi.org/project/django-rework/)
[![Python](https://img.shields.io/pypi/pyversions/django)](https://www.python.org)
[![Django](https://img.shields.io/pypi/djversions/django-rework)](https://www.djangoproject.com)
[![License](https://img.shields.io/pypi/l/django-rework)](https://opensource.org/licenses/MIT)

Rapid develop framework base on Django

# _Installation_

```bash
python3 -m pip install django-rework
```

# _Generic CLI Commands_

**Start a new project**

```bash
# recommend to append a dot(.), it will create project in current dir
# eg: initialize a new project named `pony`
rework init pony . 
rework init pony
```

**Add a app package**

```bash
rework add users
```

**Add deployment configurations**

```bash
rework deploy --init
```

**Deploy to test or production**

```bash
rework deploy
```

# Code Format

Code format using Google 的 `yapf`，recommend to install `yapf` globally：
```bash
# install yapf using pip in python3
$ python3 -m pip install yapf

# find and create soft link to `/usr/local/bin/yapf`
# find yapf execute file 
 
$ which yapf
# (/usr/local/python3.6/bin/yapf) possible location

$ ln -s /usr/local/python3.6/bin/yapf /usr/local/bin/yapf
```

### CONTRIBUTE

**Developer Environment**

```bash
pip install -r requirements_dev.txt
``` 


**Tag a new release**

tag a version:

```bash
git tag -a v0.1.0
```

push tags to remote:

```bash
git push --tags
```
