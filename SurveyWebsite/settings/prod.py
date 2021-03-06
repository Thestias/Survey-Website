import dj_database_url
from .base import *

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'whispering-island-88200.herokuapp.com', '.herokuapp.com']

DEBUG = False

# Serving Static Files

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')  # Adding WhiteNoise after the SecurityMiddleware

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'staticfiles')

DATABASE_URL = os.environ.get('DATABASE_URL')
db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)
