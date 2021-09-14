"""
Fabric tasks

Default environments is `dev`, `test`, `prod`

"""
from fabric import task

from .tasks import Hi, Environment, SetupServer, Deploy


@task
def hi(c):
    return Hi(c)()


@task
def dev(c):
    Environment(c).set_env('dev')


@task
def test(c):
    Environment(c).set_env('test')


@task
def prod(c):
    Environment(c).set_env('prod')


@task
def setup_server(c):
    """Setup a new CentOS server"""
    return SetupServer(c)()


@task
def deploy(c, infrastructure=False, requirements_update=False):
    """Deploy"""
    return Deploy(c)(
        infrastructure=infrastructure,
        requirements_update=requirements_update,
    )
