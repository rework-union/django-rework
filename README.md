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

> **rek** is the short command for `django-rework`

**Start a new project**

```bash
rek init myproject
django-rework init myproject
```

**Add a app package**

```bash
rek add users
django-rework add users
```

**Add deployment configurations**

```bash
django-rework deploy --init
```

**Deploy to test or production**

```bash
django-rework deploy
```

# Code Format 代码格式化

代码格式化使用的是 Google 的 `yapf`，建议全局安装：
```bash
# install yapf using pip in python3
$ python3 -m pip install yapf

# find and create soft link to `/usr/local/bin/yapf`
# find yapf execute file 
 
$ which yapf
# (/usr/local/python3.6/bin/yapf) possiable location

$ ln -s /usr/local/python3.6/bin/yapf /usr/local/bin/yapf
``` 

`yapf` 只需要在 PyCharm 插件市场搜索 `yapf` 可以方便的集成于 PyCharm


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
