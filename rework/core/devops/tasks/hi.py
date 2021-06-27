from ..hosts import hosts
from ...utils import say


class Hi:
    def __init__(self, c):
        self.c = c

    def __call__(self, *args, **kwargs):
        say('Hi, DevOps with Fabric is ready!', icon='🎉')
        say('loaded hosts: %s' % list(hosts.keys()), wrap='A')
