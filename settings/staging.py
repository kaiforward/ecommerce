import dj_database_url

from settings.base import *

DEBUG = False
 
# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

PAYPAL_RECEIVER_EMAIL = os.environ['PAYPAL_RECEIVER_EMAIL']
PAYPAL_TEST = True

SITE_URL = 'https://evabrudenell.herokuapp.com'
ALLOWED_HOSTS.append('evabrudenell.herokuapp.com')
# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}