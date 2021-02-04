from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p&xxz9*tkku+tb=6ka6yzq^dx_m@%_l4reh@4j1uk9mqu$f_=9'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
]  # (k9)

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # (k9)
]

INTERNAL_IPS = ("127.0.0.1", "172.17.0.1")  # (k9)...https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

try:
    from .local import *
except ImportError:
    pass
