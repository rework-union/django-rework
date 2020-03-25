from setuptools import find_packages, setup


setup(
    name='django-rework',
    version='0.1.0',
    description='Rapid develop framework base on Django',
    url='https://github.com/rework-union/django-rework',
    author='rework union',
    author_email='josh.yu_8@live.com',
    license='MIT',
    entry_points={'console_scripts': [
        'django-rework = rework.core.management:execute_from_command_line',
    ]},
    install_requires=[
        'Django>=2.0,<3.0',
        'djangorestframework==3.10.1',
    ],
    packages=find_packages(),
    zip_safe=False,
)
