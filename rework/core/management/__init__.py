import sys


def execute_from_command_line(argv=None):
    print('Hello, Rework CLI, you argv is %s' % (argv or sys.argv[:]))
