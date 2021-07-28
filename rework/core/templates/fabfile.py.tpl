from rework.core.devops.fabric_tasks import *
from rework.core.devops.hosts import loads

loads(
    'default', {
        'host': 'your-host',
        'port': 22,
        'password': 'P@ssw0rd',
        'envs': ['test', 'prod'],
        'exclude_components': [],
    }
)
