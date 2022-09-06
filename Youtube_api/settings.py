"""
Django settings for Youtube_api project.

Generated by 'django-admin startproject' using Django 2.2.24.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ed-x2-kx5pam4*j5irux=txi+kv6yh(z-en5v+s61*7n2yljbn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'youtube_app',
    'import_export',
    'users_data',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Youtube_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Youtube_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# #  Externally created database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'defaultdb',
#         'USER': 'doadmin',
#         'PASSWORD': 'AVNS_NKXIiqyP2TTA26jjk7_',
#         'HOST': 'db-postgresql-nyc3-15767-do-user-12341573-0.b.db.ondigitalocean.com',
#         'PORT': '25060',
#     }
# }


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


# STATIC_ROOT=os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
MEDIA_URL= '/upload_images/'
STATICFILES_DIRS= [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_ROOT= os.path.join(BASE_DIR, "static/upload_images")



DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880


# Divide all the models into different sections

# ADMIN_REORDER = (

# # ****** Authentication and Authorization ******

# {'app': 'auth', 'models': ('auth.User', 'auth.Group')},
# #### First group
# {
#     'app': 'youtube_app', 
#     'label': 'Data Management',
#     'models': (
#         'youtube_app.AllData', 
#         'youtube_app.AthleteProfile', 
#         'youtube_app.AthleteProfileCategory',
#         'youtube_app.Category',
#         'youtube_app.HeroSection',
#         'youtube_app.Keyword',
#         'youtube_app.RandomVideo',

#     )
# },
# # Second group: same app, but different label
# {
#     'app': 'youtube_app', 
#     'label': 'User Data',
#     'models': (
#         'youtube_app.FollowedAthletes', 
#         'youtube_app.FollowPersonality',
#         'youtube_app.WatchList',
#     )
# },
# )
