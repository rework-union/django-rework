"""
Deploy hosts

hosts is a ordered dict,
key is the `c.host`
value is
```
{
    'host': '123.123.123.123',
    'user': 'root',
    'port': '22',
    'password': 'your password',
    'envs': ['test', 'prod'],
    'exclude_components': ['redis'],
}
```

"""
import inspect
import os
from collections import OrderedDict

from fabric import Connection

from .. import devops
from ..utils import say

hosts = OrderedDict()  # all hosts loads in top of fabric file


def loads(host, value):
    hosts[host] = value

    # update project name
    previous_frame = inspect.currentframe().f_back
    filename, line_number, function_name, lines, index = inspect.getframeinfo(previous_frame)

    devops.PROJECT = os.path.dirname(filename).rsplit(os.sep, 1).pop(1).replace('-server', '')

    say(f'Project `{devops.PROJECT}` loads host successfully!', icon='✨', wrap='C')


def get_host_value(c):
    """
    get host orders:
        1. Provided in c.host
        2. Using the ENV name
        3. Using fixed `default`

    """
    try:
        host = c.host
    except (KeyError, AttributeError):
        if devops.ENV in hosts:
            host = devops.ENV
        else:
            host = 'default'

    if host not in hosts:
        raise ValueError(f'host ({host}) is not loaded yet!')

    host_value = hosts.get(host)

    # Check whether ENV and host envs match
    host_envs = host_value.get('envs', [])
    if devops.ENV not in host_value.get('envs', []):
        raise ValueError(f'Runtime env ({devops.ENV}) is not match host envs ({host_envs})')

    return host, host_value


def connect(c):
    # create a fabric connection
    host, host_value = get_host_value(c)

    return Connection(
        host_value.get('host'),
        user=host_value.get('user', 'root'),
        port=host_value.get('port', 22),
        connect_kwargs=host_value.get('connect_kwargs', {}),
    )
