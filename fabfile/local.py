from fabric.api import local

service = 'sample'
requirements_txt = 'requirements.txt'


class LocalHandler(object):
    def push(self):
        self.__update_requirements()
        self.__docker_stack_deploy()

    def __update_requirements(self):
        local('pip freeze > {}'.format(requirements_txt))
        isUpdate = local('git ls-files -m', capture=True) == requirements_txt
        if isUpdate:
            local('git add {}'.format(requirements_txt))
            local('git commit -m "{}"'.format('update requirements.txt'))

    def __docker_stack_deploy(self):
        dir_name = input('input dir_name:\t')
        yml = '{}/docker-compose.yml'.format(dir_name)
        local('docker stack deploy {0} -c {1}'.format(
            service, yml,
        ))
