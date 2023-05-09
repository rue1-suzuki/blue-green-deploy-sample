from fabric.decorators import task

from fabfile.local import LocalHandler


@task
def deploy():
    LocalHandler().push()
