import django_heroku
from .base import *

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'whispering-island-88200.herokuapp.com', '.herokuapp.com']

DEBUG = False

# Serving Static Files

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')  # Adding WhiteNoise after the SecurityMiddleware

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'staticfiles')


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["file"]},
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "./logs/django.log",
            "formatter": "app",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": True
        },
    },
    "formatters": {
        "app": {
            "format": (
                u"%(asctime)s [%(levelname)-8s] "
                "(%(module)s.%(funcName)s) %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
}


django_heroku.settings(locals())
