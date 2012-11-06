import settings
DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db/db.sqlite',          # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MIDDLEWARE_CLASSES = ['django_livejs.middleware.LivejsMiddleware','debug_toolbar.middleware.DebugToolbarMiddleware'] + settings.MIDDLEWARE_CLASSES
INSTALLED_APPS = settings.INSTALLED_APPS + ['debug_toolbar']
LIVEJS = True

INTERNAL_IPS = ('127.0.0.1',)
USE_ETAGS = True

STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static'

LIVEJS_URL = STATIC_URL+'/js/vendor/live.js' # url to live.js file