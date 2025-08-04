import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, '../.env'))


SECRET_KEY = os.getenv('SECRET_KEY')


DEBUG = True


ALLOWED_HOSTS = [] # os.getenv('ALLOWED_HOSTS').split(','),


INSTALLED_APPS = [
    'django.contrib.auth',
    'account',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'product.apps.ProductConfig',
    'tgm.apps.TgmConfig',
    'report',
    'data',
    "api",
    #"functional_tests",
    #
    'rest_framework',
    'django_filters',

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


TEMPLATEST_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATEST_DIR,],
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

WSGI_APPLICATION = 'backend.wsgi.application'


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

'''
if os.getenv('SERVER_TYPE') == 'ubuntu':
    STATIC_ROOT = '/var/www/productsite/static'
    MEDIA_ROOT = '/var/www/productsite/media'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
elif os.getenv('SERVER_TYPE') == 'local':
    STATIC_ROOT = os.path.join(BASE_DIR, '../static')
    MEDIA_ROOT = os.path.join(BASE_DIR, '../media')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
elif os.getenv('SERVER_TYPE') == 'docker':
    pass
'''

MEDIA_ROOT_TESTS = os.path.join(BASE_DIR, '../media_test')
STATIC_ROOT = os.path.join(BASE_DIR, '../static')
MEDIA_ROOT = os.path.join(BASE_DIR, '../media')
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv("BD_NAME"),
            "USER": os.getenv("BD_USER"),
            "PASSWORD": os.getenv("BD_PASSWORD"),
            "HOST": os.getenv("BD_HOST"),
            "POST": os.getenv("BD_POST")
        }
    }



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


TOKEN_BOT = os.getenv("TOKEN_BOT")
T_BOT_URL = f"https://t.me/{os.getenv('T_BOT_NAME')}?start="


ROOT_URLCONF = 'backend.urls'
LOGIN_URL = 'account:login'
LOGIN_REDIRECT_URL = '/'

PAGINATE_COUNT = 10
