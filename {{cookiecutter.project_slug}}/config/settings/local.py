"""
Local settings for {{cookiecutter.project_name}} project.

- Run in Debug mode

- Use console backend for emails

- Add Django Debug Toolbar
- Add django-extensions as app
"""

from .base import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY', default='GFQsrjWjDGMO43tyAuwvI9SuE08ird40SCW7DSZndyUkfMGdMl')

# Mail settings
# ------------------------------------------------------------------------------

EMAIL_PORT = 1025

EMAIL_HOST = 'localhost'
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.console.EmailBackend')


# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INSTALLED_APPS += ['debug_toolbar', ]

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', ]

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['django_extensions', ]

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

########## CELERY
# In development, all tasks will be executed locally by blocking until the task returns
CELERY_ALWAYS_EAGER = True
########## END CELERY


# LOGGING CONFIG
# ------------------------------------------------------------------------------
SLACK_LOG_API_KEY = env('SLACK_LOG_API_KEY',
                        default='xoxb-32068700358')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(message)s'
        },
        'simple-time': {
            'format': '%(levelname)s [%(asctime)s+0000] %(module)s %(message)s'
        }
    },
    'handlers': {
        '{{cookiecutter.project_slug}}-file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/{{cookiecutter.project_slug}}.log',
            'formatter': 'verbose',
            'when': 'D',
            'backupCount': 3,
        },
        'django-file': {
            'level': 'WARNING',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/django.log',
            'formatter': 'verbose',
            'when': 'D',
            'backupCount': 3,
        },
        'slack-error': {
            'level': 'ERROR',
            'api_key': SLACK_LOG_API_KEY,
            'class': 'slacker_log_handler.SlackerLogHandler',
            'channel': '#{{cookiecutter.project_slug}}',
            'icon_emoji': ':rocket:',
            'username': '{{cookiecutter.project_slug}} Error',
            'formatter': 'verbose',
        },
        'slack-info': {
            'level': 'INFO',
            'api_key': SLACK_LOG_API_KEY,
            'class': 'slacker_log_handler.SlackerLogHandler',
            'channel': '#{{cookiecutter.project_slug}}',
            'icon_emoji': ':small_airplane:',
            'username': '{{cookiecutter.project_slug}} Info',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['slack-error', 'django-file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        # '{{cookiecutter.project_slug}}': {
        #     'handlers': ['slack-error', '{{cookiecutter.project_slug}}-file'],
        #     'level': 'ERROR',
        #     'propagate': True,
        # },
        # 'slack.info': {
        #     'handlers': ['slack-info'],
        #     'level': 'INFO',
        #     'propagate': True,
        # }
    },
}

# Your local stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------
