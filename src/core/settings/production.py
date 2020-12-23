import os
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'true').lower() == "true"

DEFAULT_CONNECTION = dj_database_url.parse(os.environ.get('DATABASE_URL'))
DEFAULT_CONNECTION.update({'CONN_MAX_AGE': 600})
DATABASES = {'default': DEFAULT_CONNECTION}
ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = os.environ.get('CORS_ORIGIN_ALLOW_ALL', 'true').lower() == 'true'

REG_CHECK_API_USERNAME = os.environ.get('REG_CHECK_API_USERNAME')

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')

# SENDGRID CONFIG
SENDGRID_API_KEY = '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'
SENDGRID_TEMPLATE_ID = 'd-870e6d47f7ca49b7a3784ee8d25005f6'

# EMAIL CONFIG
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
EMAIL_PORT = os.environ.get('EMAIL_PORT')

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')