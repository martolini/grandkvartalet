"""
Django settings for grandkvartalet project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
PRODUCTION = 'cauchy' in socket.gethostname()


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v_99gv@icn5rtlygo8ezm&05lhy-@$zsqwkz&gc*5m=(3m&whr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not PRODUCTION

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'pyjade',

    'grandkvartalet.core.comingsoon',
    'grandkvartalet.core.landing',
    'grandkvartalet.app.contact',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'grandkvartalet.urls'

WSGI_APPLICATION = 'grandkvartalet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

if PRODUCTION:
    STATIC_ROOT = '/opt/grenv/static/'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'no'

TIME_ZONE = 'Europe/Oslo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


# TEMPLATE LOADERS PYJADE

TEMPLATE_LOADERS = (
    ('pyjade.ext.django.Loader',(
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

# EMAIL
EMAIL_USE_TLS = True
EMAIL_PORT = 587

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'grandkvartalet.web@gmail.com'
EMAIL_HOST_PASSWORD = 'GrandkvartaletWeb'

