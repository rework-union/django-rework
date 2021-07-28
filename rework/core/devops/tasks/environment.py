from ... import devops


class Environment:
    def __init__(self, c):
        self.c = c

    @staticmethod
    def set_env(env):
        devops.ENV = env
