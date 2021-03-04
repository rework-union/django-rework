from setuptools import find_packages, setup
from rework import core

# version Operators
# https://pip.pypa.io/en/latest/user_guide/#fixing-conflicting-dependencies
INSTALL_REQUIREMENTS = [
    'Django>=2.2,<3.0',
    'django-cors-headers==3.1.0',
    'django-filter>=2.0,<3.0',
    'django-mysql==3.2.0',
    'djangorestframework>=3.10.1,<4.0',
    'fabric~=2.5',
    'Markdown~=3.1',
    'mysqlclient==1.4.6',
    'Pillow>=6.2.2,<=8.1.0',
    'drf-nested-routers~=0.91',
    'drf-yasg~=1.17',
    'wechatpy~=1.8',
]

setup(
    name='django-rework',
    version=core.__version__,
    description='Rapid develop framework base on Django',
    url='https://github.com/rework-union/django-rework',
    author='rework union',
    author_email='josh.yu_8@live.com',
    license='MIT',
    entry_points={
        'console_scripts':
            [
                'rework = rework.core.management:execute_from_command_line',
            ]
    },
    install_requires=INSTALL_REQUIREMENTS,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
