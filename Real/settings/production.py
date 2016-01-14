#local.py
form .base import *

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1' , 'reynald0.pythonanywhere.com']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'real_db',
        'USER': 'Reynald0',
        'PASSWORD': 'R3ynaldit095',
        'HOST': 'Reynald0.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
