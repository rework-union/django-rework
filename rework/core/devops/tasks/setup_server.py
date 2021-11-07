"""
Setup server configurations from a new server
Support CentOS 7
"""
from ..hosts import hosts, get_host_value, connect
from ...utils import say


class SetupServer:
    def __init__(self, c):
        self.c = connect(c)
        self.host_value = get_host_value(c)[1]

    def __call__(self, *args, **kwargs):
        self.setup_python3()
        self.check_components('nginx') and self.setup_nginx()
        self.check_components('supervisor') and self.setup_supervisor()
        self.check_components('mysql') and self.setup_mysql()
        self.check_components('redis') and self.setup_redis()

    def check_components(self, component):
        return component not in self.host_value.get('exclude_components', [])

    def setup_python3(self):
        """Install python3 and uWSGI"""
        version = '3.7.9'
        major_version = version.rsplit('.', 1)[0]
        # Install Python
        self.c.run('yum -y update')
        self.c.run('yum groupinstall "Development tools"')
        try:
            self.c.run('yum -y install wget gcc make zlib-devel')
        except Exception as ex:
            print('ex', ex)
        self.c.run(f'wget https://www.python.org/ftp/python/{version}/Python-{version}.tgz')
        self.c.run(f'tar xzf Python-{version}.tgz')
        self.c.run(
            'cd Python-{version} && ./configure --with-ssl --prefix=/usr/local && make altinstall'
        )
        self.c.run(f'ln -s /usr/local/bin/python{major_version} /usr/bin/python3')
        self.c.run('python3 -V')
        say('Clean up Python setup files')
        self.c.run('rm -rf Python-{version}')

        # Install Gunicorn
        pypi_mirror_suffix = ' -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com'
        self.c.run(f'python3 -m pip install gunicorn {pypi_mirror_suffix}')

    def setup_nginx(self):
        # Install Nginx
        self.c.run('yum install -y nginx')

    def setup_supervisor(self):
        # Install Supervisor in Python 2
        self.c.run('curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py -o get-pip.py')
        self.c.run('python get-pip.py')
        self.c.run('python -m pip install supervisor==4.1.0')

    def setup_mysql(self):
        download_url = 'https://dev.mysql.com/get/mysql80-community-release-el7-1.noarch.rpm'
        self.c.run(f'sudo rpm -Uvh {download_url}')
        self.c.run('sudo yum --enablerepo=mysql80-community install mysql-community-server')

    def setup_redis(self):
        version = '4.0.14'
        download_url = f'http://download.redis.io/releases/redis-{version}.tar.gz'
        self.c.run(f'curl -o redis-{version}.tar.gz {download_url}')
        self.c.run(f'tar -zxvf redis-{version}.tar.gz')

        self.c.run(f'cd redis-{version} & make')
        self.c.run(f'cd src && make install PREFIX=/usr/local/redis')

        self.c.run(f'mkdir -p /usr/local/redis/conf')
        self.c.run(f'cp redis-{version}/redis.conf /usr/local/redis/conf')

        # start redis
        self.c.run('cd /usr/local/redis && bin/redis-server ./conf/redis.conf')
