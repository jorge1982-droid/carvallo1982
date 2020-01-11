from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['https://djangoblogdeveloperjc.herokuapp.com']
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
         'USER':'zbmiyzfxwzbyyf',
         'DATABASE':'d6hcgj74pr4971',
         'HOST':'ec2-107-20-198-176.compute-1.amazonaws.com',
         'PASSWORD':'ea6d8a7cd9c63e3791b9e1e734818b186ebffc41528c3a161049ac13b89e5bbe',
         'PORT':5432,



    }
}
