"""
Fabric tasks

Default environments is `dev`, `test`, `prod`

"""
from fabric import task


@task
def hi(c):
    print(f'Hi, DevOps with Fabric is ready! {c.host}')


@task
def deploy(c):
    """Deploy"""
    pass
