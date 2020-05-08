import os
from setuptools import find_packages, setup

INSTALL_REQUIREMENTS = [
    'Django>=2.2,<3.0',
    'django-cors-headers==3.1.0',
    'django-filter==2.0.0',
    'django-mysql==3.2.0',
    'djangorestframework==3.10.1',
    'fabric==2.5.0',
    'Markdown==3.1.1',
    'mysqlclient==1.4.6',
    'Pillow==6.2.2',
    'drf-nested-routers==0.91',
    'drf-writable-nested==0.5.4',
    'drf-yasg==1.17',
    'wechatpy==1.8',
]


setup(
    name='django-rework',
    version='0.1.1',
    description='Rapid develop framework base on Django',
    url='https://github.com/rework-union/django-rework',
    author='rework union',
    author_email='josh.yu_8@live.com',
    license='MIT',
    entry_points={'console_scripts': [
        'django-rework = rework.core.management:execute_from_command_line',
    ]},
    install_requires=INSTALL_REQUIREMENTS,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
