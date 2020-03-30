# -*- coding: UTF-8 -*-
import os
import shutil

from .base_management import BaseCommand

class DeployCommand(BaseCommand):
    def handle(self, params):
        if params == ['--init']:
            try:
                working_dir = os.path.join(self.base_dir, 'deploy')
                core_dir = os.path.join(self.core_dir, 'deploy')
                shutil.copytree(core_dir, working_dir)
            except Exception as e:
                print (e)
        else:
            pass


    def __call__(self, params):
        return self.handle(params)