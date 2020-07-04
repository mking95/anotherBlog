from .base import *
DEBUG = False
ADMINS = (
    ('Mike K', 'webmaster@nyntofive.com'),
)

ALLOWED_HOSTS = ['nyntofive.com','.nyntofive.com','localhost','nynode1']
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'myblog',
       'USER': 'nyndb',
       'PASSWORD': os.environ.get('DB_PASS'),
   }
}


DATABASES = {
    'default': {
    }
}
