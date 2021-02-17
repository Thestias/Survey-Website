from .base import *
from dotenv import load_dotenv

# Loading Dot-Enviroment Variables
dotenv_path = os.path.join(os.path.dirname(BASE_DIR), '.env')
load_dotenv(dotenv_path)

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']


# Serving Static Files

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')  # Adding WhiteNoise after the SecurityMiddleware

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'staticfiles')
