"""
Django settings for news project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
#import modules
from pathlib import Path
import environ
import boto3
import json
from botocore.exceptions import NoCredentialsError

#AWS Secret Manager configuration
AWS_SECRETS_MANAGER_REGION_NAME = 'us-east-2'  # Replace with your AWS region
AWS_SECRETS_MANAGER_SECRET_NAME = 'mynewappsecretkey'  # Replace with the name of your secret
AWS_ACCESS_KEY_ID = 'AKIAQ3S3JBTA2OHE7BGA'  # Replace with your AWS secret access key
AWS_SECRET_ACCESS_KEY = 'ufmvicj9A6Kk/WFoVjl60Ut6GTU/O/3pjzcPqWd4'  # Replace with the name of your secret

# Function to retrieve secrets from AWS Secret Manager
def get_secret_value():
    secret_name = AWS_SECRETS_MANAGER_SECRET_NAME
    region_name = AWS_SECRETS_MANAGER_REGION_NAME
    
    try:
        # Create a Secrets Manager client with AWS credentials
        session = boto3.session.Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )
        client = session.client(
            service_name='secretsmanager', 
            region_name=region_name
        )
        # Get the secret value
        response = client.get_secret_value(SecretId=secret_name)
        secret_value = response['SecretString']
        
        return secret_value
    
    except NoCredentialsError:
        print("Unable to access AWS credentials.")

#set env
# env = environ.Env()
# environ.Env.read_env()

# Retrieve the secret values
SECRET_VALUES = get_secret_value()

# Parse the secret values string into a dictionary
secret_values_dict = json.loads(SECRET_VALUES)

# Access the specific secret key
#print(secret_values_dict["SECRET_KEY"])

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# root NEWS folder
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# when deploy project , secret_key should not be leaked
SECRET_KEY=secret_values_dict["SECRET_KEY"]
DEBUG = True
# SECURITY WARNING: don't run with debug turned on in production!
# important
# django tell what error you have faced
# when service to customer make this to False / make secure


# using when deploying project
# put domain
ALLOWED_HOSTS = []


# Application definition
# plugin and play 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'listings'
]
#security setting
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#pointing urls.py file inside of news folder
ROOT_URLCONF = 'news.urls'

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


WSGI_APPLICATION = 'news.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# important settng 
# database is gonna be file
# change to other database for deploying
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''


# Amazon RDS PostgreSQL database (Live)

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql',

        'NAME': secret_values_dict['DATABASE_NAME'],

        'USER' : secret_values_dict['DATABASE_USER'],

        'PASSWORD' : secret_values_dict['DATABASE_PASS'],

        'HOST' : secret_values_dict['DATABASE_HOST'],

        'PORT' : secret_values_dict['DATABASE_PORT'],
    }

}




# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/
# translation
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = 'media'

# method 1
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# less than 4.0 version
#method 2
#STATICFILES_DIRS = os.path.join(BASE_DIR , 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
