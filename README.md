# Django Rework

[![Downloads](https://pepy.tech/badge/django-rework)](https://pepy.tech/project/django-rework)
[![PyPI](https://img.shields.io/pypi/v/django-rework)](https://pypi.org/project/django-rework/)
[![Python](https://img.shields.io/pypi/pyversions/django-rework)](https://www.python.org)
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
django-rework init projectname
```

**Add deployment configurations**

```bash
django-rework deploy --init
```

<br>

# _RoadMap_

`v0.4`

<u>Expected release at 2020/6/30</u>

> - [ ] Add contrib app: O2O (app name still uncertain)
>
> - [ ] Add contrib app: shopcart (app name still uncertain)

`v0.3`

<u>Expected release at 2020/5/31</u>

> - [ ] Docs for core and exists Apps
>
> - [ ] Extend features of contrib apps: users / paid content

`v0.2`

<u>Expected release at 2020/4/30</u>

> - [ ] Code style: black
>
> - [ ] Add test
>
> - [ ] Optimized CLI console logs
>
> - [ ] Add contrib app: paid content (app name still uncertain)

`v0.1`

<u>Expected release at 2020/4/10</u>

> - [x] Command `init`: start a project
>
> - [x] Command `add`: add contrib apps
>
> - [x] Copy deploy files into project, using `django-rework deploy --init`
>
> - [ ] Add contrib app: users
