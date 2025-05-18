import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-y(t9q2a@r&xg2bcmdalx)htox-wmer%x%&(j^!s8h0)l9he8mx')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_browser_reload',

    #app
    'accounts',
    'issue',
    'chat',
    'channels',
]

# Channel layer
ASGI_APPLICATION = 'community_guardian.asgi.application'

# In development, use InMemoryChannelLayer
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add Whitenoise before other middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]

ROOT_URLCONF = 'community_guardian.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'community_guardian.wsgi.application'

# Database setup
# Use SQLite with different paths for local vs production
if DEBUG:
    # Local development: use SQLite in project directory
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    # Production: use SQLite in the project directory
    # Render has a persistent disk at /opt/render/project/src/
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Use WhiteNoise for static files in production
if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configure Django's logging based on environment
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
os.makedirs(LOGS_DIR, exist_ok=True)  # Create logs directory if it doesn't exist

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGS_DIR, 'django_errors.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# import os
# from pathlib import Path

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-y(t9q2a@r&xg2bcmdalx)htox-wmer%x%&(j^!s8h0)l9he8mx')

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# ALLOWED_HOSTS = ['*']

# # Application definition
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',

#     'django_browser_reload',

#     #app
#     'accounts',
#     'issue',
#     'chat',
#     'channels',
# ]

# # Channel layer
# ASGI_APPLICATION = 'community_guardian.asgi.application'

# # In development, use InMemoryChannelLayer
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels.layers.InMemoryChannelLayer",
#     },
# }

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',  # Add Whitenoise before other middleware
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'django_browser_reload.middleware.BrowserReloadMiddleware',
# ]

# ROOT_URLCONF = 'community_guardian.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'community_guardian.wsgi.application'

# # Database setup
# # Use SQLite with different paths for local vs production
# if DEBUG:
#     # Local development: use SQLite in project directory
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }
# else:
#     # Production: use SQLite in the persistent disk location
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': os.path.join('/var/data', 'db.sqlite3'),
#         }
#     }

# # Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# # Internationalization
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# # Static files (CSS, JavaScript, Images)
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# # Use WhiteNoise for static files in production
# if not DEBUG:
#     STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# # Media files
# MEDIA_URL = '/media/'
# if DEBUG:
#     MEDIA_ROOT = BASE_DIR / 'media'
# else:
#     MEDIA_ROOT = '/var/media'

# # Default primary key field type
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # Configure Django's logging based on environment
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '{levelname} {asctime} {module} {message}',
#             'style': '{',
#         },
#         'simple': {
#             'format': '{levelname} {message}',
#             'style': '{',
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'INFO',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose',
#         },
#     },
#     'root': {
#         'handlers': ['console'],
#         'level': 'INFO',
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#     },
# }
# # if DEBUG:
# #     # Local development logging
# #     LOGGING = {
# #         'version': 1,
# #         'disable_existing_loggers': False,
# #         'formatters': {
# #             'verbose': {
# #                 'format': '{levelname} {asctime} {module} {message}',
# #                 'style': '{',
# #             },
# #         },
# #         'handlers': {
# #             'console': {
# #                 'level': 'INFO',
# #                 'class': 'logging.StreamHandler',
# #                 'formatter': 'verbose',
# #             },
# #             'file': {
# #                 'level': 'ERROR',
# #                 'class': 'logging.FileHandler',
# #                 'filename': os.path.join(BASE_DIR, 'django_errors.log'),  # Use project directory
# #                 'formatter': 'verbose',
# #             },
# #         },
# #         'loggers': {
# #             'django': {
# #                 'handlers': ['console', 'file'],
# #                 'level': 'INFO',
# #                 'propagate': True,
# #             },
# #         },
# #     }
# # else:
#     # Production logging
#     # LOGGING = {
#     #     'version': 1,
#     #     'disable_existing_loggers': False,
#     #     'formatters': {
#     #         'verbose': {
#     #             'format': '{levelname} {asctime} {module} {message}',
#     #             'style': '{',
#     #         },
#     #     },
#     #     'handlers': {
#     #         'console': {
#     #             'level': 'INFO',
#     #             'class': 'logging.StreamHandler',
#     #             'formatter': 'verbose',
#     #         },
#     #         'file': {
#     #             'level': 'ERROR',
#     #             'class': 'logging.FileHandler',
#     #             'filename': '/var/data/django_errors.log',  # Use persistent disk
#     #             'formatter': 'verbose',
#     #         },
#     #     },
#     #     'loggers': {
#     #         'django': {
#     #             'handlers': ['console', 'file'],
#     #             'level': 'INFO',
#     #             'propagate': True,
#     #         },
#     #     },
#     # }