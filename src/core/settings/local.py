SECRET_KEY = '*j_!-@24!m06o33*8u_wqrr^%oskp0uc_@=d!kxwjh6@xdxojo'

DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'car_insurance',
        'USER': 'postgres',
        'PASSWORD': 'bhushan',
        'HOST': 'localhost',
        'PORT': ''  
    }
}'''


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "bhushan_wfh_rest",
        "USER": "root",
        "PASSWORD": "bhushan",
        "HOST": "127.0.0.1",
    }
}

ALLOWED_HOSTS = ['*']

REG_CHECK_API_USERNAME = ""
CELERY_BROKER_URL = "" 

SENDGRID_API_KEY = "" 
SENDGRID_TEMPLATE_ID = "" 

EMAIL_HOST = ""
EMAIL_HOST_USER = "" 
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = ""