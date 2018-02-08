import os
from pathlib import Path


def secret(key, default=None):
    '''
    Get a secret from the environment or from the filesystem.
    '''
    if key in os.environ:
        return os.environ.get(key)
    else:
        secret_file_name = '/run/secrets/{}'.format(key)
        if os.path.exists(secret_file_name):
            return Path(secret_file_name).read_text()
    return default


# Gunicorn settings.

HOST = secret('APP_HOST', '0.0.0.0')

PORT = secret('APP_PORT', 8000)

bind = '{}:{}'.format(HOST, PORT)

loglevel = secret('GUNICORN_LOGLEVEL', 'info')

reload = secret('GUNICORN_RELOAD', True) in [True, 'True']

syslog = secret('GUNICORN_SYSLOG', True) in [True, 'True']

worker_class = secret('GUNICORN_WORKER_CLASS', 'gevent')

try:
    workers = int(secret('GUNICORN_WORKERS', '2'))
except (TypeError, ValueError):
    workers = 1
