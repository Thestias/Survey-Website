import django_heroku
from .base import *

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'whispering-island-88200.herokuapp.com', '.herokuapp.com']

DEBUG = False

# Serving Static Files

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')  # Adding WhiteNoise after the SecurityMiddleware

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'staticfiles')

django_heroku.settings(locals())
