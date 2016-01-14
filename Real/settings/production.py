#local.py
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1' , 'reynald0.pythonanywhere.com']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'real_db.db'),
    }
}
