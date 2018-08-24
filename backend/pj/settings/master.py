import dj_database_url

from .base import *  # noqa:F401,F403 # pylint:disable=W0401,W0614

DEBUG = True

db_from_env = dj_database_url.config(conn_max_age=500, ssl_require=True)
DATABASES['default'] = db_from_env

try:
    from .local import *  # noqa:F401,F403 # pylint:disable=W0401,W0614
except ImportError:
    pass
