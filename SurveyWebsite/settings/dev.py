from .base import *
from dotenv import load_dotenv, find_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env')
load_dotenv(dotenv_path)
# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = 'vp-$4%k$&^lvw0ls5be4wa-=$s%nsp##$kan+b3epla95q!y3)'
DEBUG = True

ALLOWED_HOSTS = []

# EMAIL SETTINGS

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
