import os
import subprocess

def migrate(params):
    """ migrate db """    

    print('Start to migrate DB')

    base_dir = os.getcwd()
    manage_dir = None

    for root, dirs, files in os.walk(base_dir):
        if os.path.exists(os.path.join(root, 'manage.py')):
            manage_dir = os.path.join(root, 'manage.py')
            break 

    if manage_dir:
        result = subprocess.run(['python3', manage_dir, 'migrate'])
        if result.returncode != 0:
            print('Migrate DB failed!')
        else:
            print('Migrate DB successed!')
    else:
        print('Not found manage.py!')