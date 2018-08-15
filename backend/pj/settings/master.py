from .base import *  # noqa:F401,F403 # pylint:disable=W0401,W0614

DEBUG = False

try:
    from .local import *  # noqa:F401,F403 # pylint:disable=W0401,W0614
except ImportError:
    pass
