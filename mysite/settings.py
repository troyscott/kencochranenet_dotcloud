# Django settings for mysite project.
import os

import json
with open('/home/dotcloud/environment.json') as f:
  env = json.load(f)

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS
SEND_BROKEN_LINK_EMAILS = True

# Site owner will be used throughout the site.
# This should represent the site author.
SITE_OWNER = "SITE_OWNER"
SITE_TITLE = "My awesome blog"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogdb',
        'USER': env['DOTCLOUD_DB_MYSQL_LOGIN'],
        'PASSWORD': env['DOTCLOUD_DB_MYSQL_PASSWORD'],
        'HOST': env['DOTCLOUD_DB_MYSQL_HOST'],
        'PORT': int(env['DOTCLOUD_DB_MYSQL_PORT']),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': env['DOTCLOUD_CACHE_REDIS_HOST']+':'+env['DOTCLOUD_CACHE_REDIS_PORT'],
        'OPTIONS': {
            'DB': 1,
            'PASSWORD': env['DOTCLOUD_CACHE_REDIS_PASSWORD'],
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        },
    },
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
USE_I18N = False

SITE_ID = 1

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/dotcloud/data/media/'
STATIC_ROOT = '/home/dotcloud/data/static/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# Make this unique, and don't share it with anybody.
# This should be defined in the local_settings.py file
SECRET_KEY = '61y_pbt123b&#sdsjwe(aa%^x==--82qmp%rz9&398v*yy0s34i1=b'

# These should be the API key (http://disqus.com/api/get_my_key/) and website
# shortname from your DISQUS account.
DISQUS_API_KEY = "deploy.DISQUS_API_KEY"
DISQUS_WEBSITE_SHORTNAME = "deploy.DISQUS_WEBSITE_SHORTNAME"

# http://www.viglink.com used for affiliate link tracking
VIGLINK_KEY = "deploy.VIGLINK_KEY"
GOOGLE_ANALYTICS_CODE = "deploy.GOOGLE_ANALYTICS_CODE"

# http://addthis.com sharing widget.
ADDTHIS_USERNAME = "deploy.ADDTHIS_USERNAME"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates/'),
)

# Overrides the default in order to remove I18N processor
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'mysite.context_processors.CurrentSite',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'activitysync',
    'blog',
    'disqus',
    'metaweblog',
    'tagging',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.sitemaps',
    'django.contrib.markup',
    'south',
)

# Activity sync settings
ACTIVITYSYNC_PROVIDERS = (
    #'activitysync.providers.googlereader.GoogleReaderProvider',
    'activitysync.providers.twitterprovider.TwitterUserProvider',
    'activitysync.providers.redditprovider.RedditProvider',
)

#ACTIVITYSYNC_SETTINGS = "deploy.ACTIVITYSYNC_SETTINGS"


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': '/var/log/supervisor/blogapp.log',
            'maxBytes': 1024*1024*25, # 25 MB
            'backupCount': 5,
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'log_file', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console', 'log_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console', 'log_file', 'mail_admins'],
            'level': 'INFO',
            'propagate': False,
        },
        # Catch All Logger -- Captures any other logging
        '': {
            'handlers': ['console', 'log_file', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'