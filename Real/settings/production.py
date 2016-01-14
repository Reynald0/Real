#local.py
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1' , 'reynald0.pythonanywhere.com']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
