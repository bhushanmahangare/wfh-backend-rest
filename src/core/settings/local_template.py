# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': ''
    }
}

ALLOWED_HOSTS = []

# SENDGRID CONFIG
SENDGRID_API_KEY = ''
SENDGRID_TEMPLATE_ID = ''

# EMAIL CONFIG
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

# CELERY CONFIG
CELERY_BROKER_URL = ''