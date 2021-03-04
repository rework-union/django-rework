import os
import sys

from . import project, app, deploy, migrate

COMMANDS = {
    'init': project.init,
    'add': app.add,
    'deploy': deploy.DeployCommand(),
    'migrate': migrate.migrate
}


def execute_from_command_line(argv=None):
    argv = argv or sys.argv[:]
    print(f'{os.linesep} 🏂 Hello, Rework CLI, you argv is {argv}{os.linesep}')

    command = argv[1]

    if command in COMMANDS:
        COMMANDS.get(command)(argv[2:])
    else:
        print(f'{os.linesep} 🌶️ Command not found!{os.linesep}')
