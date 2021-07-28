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

### Start a new project

```bash
# recommend to append a dot(.), it will create project in current dir
# eg: initialize a new project named `pony`
rework init pony . 
rework init pony
```

### Add App

```bash
rework add users
```

### Add deployment configurations

```bash
rework deploy --init
```

### Deploy to test or production

```bash
rework deploy
```

# App docs

| App      | Description | docs |
| ----------- | ----------- | ----------- |
| users      | Users system       | [users.md](docs/users.md) |


# DevOps Fabric scripts 

## Setup hosts

`django-rework` deal with DevOps using `Fabric`. You should add hosts configurations in `fabfile.py`.

```python
from rework.core.devops.hosts import loads

# The first argument `default` is host alias
# `user` is optional, default value is `root`
# `exclude_components` is optional, it's been used in `fab setup_server`
loads(
    'default', {
        'host': 'your-server-ip',
        'port': 22,
        'user': 'root',
        'password': 'server-password',
        'envs': ['test', 'prod'],
        'exclude_components': ['redis'],
    }
)
```

You can change host alias as you like: `web1` etc.
```bash
fab -H web1 deploy
```

if not `-H` provided, the default alias will use according the order below:
1. environment name: `dev`, `test`, `prod`
2. `default`

## Deploy environments

By default, environments is `dev`, `test`, `prod`, every environment name is a generic fabric tasks.

```bash
# deploy to `test` environment
fab test deploy
```

If you want to update requirements, you should add arguments `-r` or `--requirements_update`
```bash
fab test deploy -r
```


# _Code Format_

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

# _CONTRIBUTE_

### Developer Environment

```bash
pip install -r requirements_dev.txt
``` 

### Run tests

```bash
python ./tests/runtests.py
```


### Tag a new release

tag a version:

```bash
git tag -a v0.1.0
```

push tags to remote:

```bash
git push --tags
```
