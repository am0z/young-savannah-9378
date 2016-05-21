import os
import environ

root = environ.Path(__file__) - 2
env = environ.Env(DEBUG=(bool, False),)

try:
    environ.Env.read_env(root.file('.env'))
except IOError:
    pass

DEBUG = env('DEBUG')

DATABASES = {
    'default': env.db()
}

CACHES = {
    'default': env.cache(),
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']


STATIC_ROOT = root.path('staticfiles')()

SECRET_KEY = 'mvy!eh^nl!19#)!7lt#&cn&%b^8w2^ml8r#_)2#!r+4j)@*px#'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'crispy_forms',
    'opbeat.contrib.django',
    'young',
    'youngsters',
    'contact',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
)

ROLLBAR = {
    'access_token': os.environ.get('ROLLBAR_ACCESS_TOKEN'),
    'environment': 'development' if DEBUG else 'production',
    'branch': 'master',
    'root': root(),
}

OPBEAT = {
    'ORGANIZATION_ID': '125f2995a2cc45639619abaa6db2d7d8',
    'APP_ID': '92e7437bc4',
    'SECRET_TOKEN': '25d697ad26cc3c73d02d4b1b6a37800cdd083b86',
}

ROOT_URLCONF = 'young.urls'

WSGI_APPLICATION = 'young.wsgi.application'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

CONTACT_EMAIL = 'am0z@ya.ru'
