from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!na_9wwv23d)-3c3vnr-b)8buke*6c#lkrhw5k7ai4i6rc$=a0'
ALLOWED_HOSTS = ['*']  # Permite todas las solicitudes, no recomendado para producción
 
# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
