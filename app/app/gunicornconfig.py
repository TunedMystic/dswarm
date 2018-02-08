# Gunicorn settings.

HOST = '0.0.0.0'

PORT = 8000

bind = '{}:{}'.format(HOST, PORT)

loglevel = 'debug'

reload = True

syslog = False

worker_class = 'gevent'

workers = 4
