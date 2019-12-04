"""
Django settings for antusu_experimento1 project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_ROOT =  os.path.join(BASE_DIR, 'media') 
MEDIA_URL = '/media/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'he(=h0(dj&@r!m-0kkkx)qt)4-0yt@lj3)_xg@(k78kga8%u-a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['127.0.0.1','172.24.42.93','172.24.42.99','backend','172.24.41.183','35.173.231.140','172.31.85.234','dbantusu.cbexlpsyzfjf.us-east-1.rds.amazonaws.com','localhost']

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shoe',
    'purchase',
    'suppliers',
    'clients',
    'shoeInstance',
    'social_django',
    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'antusu_experimento1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'antusu_experimento1', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'antusu_experimento1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'antusuDB',
        'USER': 'antusuUser',
        'PASSWORD': 'isis2503',
        'HOST': 'antusu-db.ckuagagti7ud.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static', 'media')

# STATICFILES_DIRS = (
#     os.path.join(PROJECT_ROOT, 'static'),
# )
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]

#Esta es la parte que se usa para poder implementar auth0
LOGIN_URL = "/login/auth0"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "https://isis2503-carlosinfante98.auth0.com/v2/logout?returnTo=http%3A%2F%2F35.174.170.28:8000"

SOCIAL_AUTH_TRAILING_SLASH = False  # Remove end slash from routes
SOCIAL_AUTH_AUTH0_DOMAIN = 'isis2503-carlosinfante98.auth0.com'
SOCIAL_AUTH_AUTH0_KEY = 'RYxlSZSeKPvmZwsCpXhM6dz8xPPPpewR'
SOCIAL_AUTH_AUTH0_SECRET = 'IR_Oz3pk_DgHACkTS60Oqthpo6zDd_XoBUnTi77FMziCJkThVP0VTTmTE4UE4DeP'

SOCIAL_AUTH_AUTH0_SCOPE = [
    'openid',
    'profile'
]
AUTHENTICATION_BACKENDS = {
    'antusu_experimento1.auth0backend.Auth0',
    'django.contrib.auth.backends.ModelBackend',
}

PATH_VAR = "http://0.0.0.0:8000/shoes/suppliershoes"
