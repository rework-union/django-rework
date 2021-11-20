import os
import sys

from . import project, app, deploy, migrate
from ..utils import say

COMMANDS = {
    'init': project.init,
    'add': app.add,
    'deploy': deploy.DeployCommand(),
    'migrate': migrate.migrate
}


def execute_from_command_line(argv=None):
    argv = argv or sys.argv[:]
    say(f'Hello, Rework CLI, you argv is {argv}', icon='🏂', wrap='B')

    command = argv[1]

    # Hack the `init` command,
    # append startproject path '.' to argv when command is init
    if command == 'init':
        argv.append('.')
        say(f'Oh hacked, you argv is {argv}', icon='🏂', wrap='A')

    if command in COMMANDS:
        COMMANDS.get(command)(argv[2:])
    else:
        say(f'Command not found!', icon='🌶️ ', wrap='C')
