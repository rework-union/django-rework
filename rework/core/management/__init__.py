import sys

from . import project, app


COMMANDS = {
    'init': project.init,
    'add': app.add,
}


def execute_from_command_line(argv=None):
    argv = argv or sys.argv[:]
    print('Hello, Rework CLI, you argv is %s' % argv)

    command = argv[1]

    if command in COMMANDS:
        COMMANDS.get(command)(argv[2:])
    else:
        print('[Error] Command not found!')
