"""
Fabric tasks

Default environments is `dev`, `test`, `prod`

"""
from fabric import task
from .hosts import hosts, get_host_value
from ..utils import say
from .tasks import Hi, SetupServer


@task
def hi(c):
    return Hi(c)()


@task
def setup_server(c):
    """Setup a new CentOS server"""
    return SetupServer(c)()


@task
def deploy(c):
    """Deploy"""
    pass
