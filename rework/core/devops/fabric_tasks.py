from fabric import task


@task
def hi(c):
    print('Hi, DevOps with Fabric is ready!')
