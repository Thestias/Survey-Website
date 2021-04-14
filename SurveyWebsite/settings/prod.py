import django_heroku
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['whispering-island-88200.herokuapp.com', '*.herokuapp.com']

# Serving Static Files

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')  # Adding WhiteNoise after the SecurityMiddleware

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'staticfiles')

django_heroku.settings(locals())
