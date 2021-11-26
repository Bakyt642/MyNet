"""
Django settings for NetShoot project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
# import django_heroku
import os
from pathlib import Path

from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hd)c&j%e6omasl!l8oyirq=&!1&afwbr835oe0g9=(^g$upm2$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS = ['netshoot.kz', 'www.netshoot.kz', 'https://netshoot.kz', 'localhost', '127.0.0.1']
ALLOWED_HOSTS = ['netshoot.kz','127.0.0.1', 'sarmanovbakyt-blog.herokuapp.com','sarmanovbakyt-blog.herokuapp.com/en/']

# Application definition

INSTALLED_APPS = [
     'debug_toolbar',
    'taggit',
    'modeltranslation',
    'django.contrib.postgres',
    # 'taggit_autosuggest',
    "captcha",
    'ckeditor_uploader',
    'ckeditor',
    'crispy_forms',
    'django_extensions',
    'social_django',
    'account.apps.AccountConfig',
    'blog.apps.BlogConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    # 'jquery',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'NetShoot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'NetShoot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blogdb',
        'USER': 'bacho',
        'PASSWORD': 'bacho',
        #   'ENGINE': 'django.db.backends.sqlite3',
        #   'NAME': BASE_DIR / 'db.sqlite3',
}
}
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# LANGUAGES = [
#   ('en', _('English')),
#   ('ru', _('Russian')),
#   ]
gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('ru', gettext('Russian')),
)
#LANGUAGE_CODE = 'en-us'

LOCALE_PATHS = (
os.path.join(BASE_DIR, 'locale/'),
)




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
STATICFILES_DIR =[
    os.path.join(BASE_DIR, 'static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = 'post_list'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2',
]

SOCIAL_AUTH_FACEBOOK_KEY = '570301917615150' # Facebook App ID pass 'ncoc_123'
SOCIAL_AUTH_FACEBOOK_SECRET = '34f1740b02f60d17cc8a697e0f6ad0a4' # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']



SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '541488547966-7e1gtkvg9ki1cucbrcf8senfu57p3889.apps.googleusercontent.com' # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'PIBgg-mdSfPIpvWsw2lGishd' # Google Consumer Secret
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
# CKEDITOR_BASEPATH = "/static/"
# CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = 'bootstrap4'
CKEDITOR_ALLOW_NONIMAGE_FILES = True
CKEDITOR_RESTRICT_BY_USER = False
# CKEDITOR_IMAGE_BACKEND = "pillow"
# CKEDITOR_THUMBNAIL_SIZE = (300, 300)
# CKEDITOR_FORCE_JPEG_COMPRESSION = True
# CKEDITOR_IMAGE_QUALITY = 95 #The image quality, on a scale from 1 (worst) to 95 (best). The default is 75. Values above 95 should be avoided; 100 disables portions of the JPEG compression algorithm and results in large files with hardly any gain in image quality.
THUMBNAIL_DEBUG = True

# CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
# CKEDITOR_JQUERY_URL = 'bootstap/js/bootstrap.bundle.CKEDITOR_CONFIGS = {
#         'default': {
#             'toolbar': 'full',
#              'extraPlugins': ','.join([
#                 'uploadimage', # the upload image feature
#                  'image',
#                  'uploadwidget'
#             ]),
#
#         },
# }min.js'
# CKEDITOR_CONFIGS = {
#         'default': {
#             'toolbar': 'full',
#              'extraPlugins': ','.join([
#                 'uploadimage', # the upload image feature
#                  'image',
#                  'uploadwidget'
#             ]),
#
#         },
# }
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'full',
#          'contentsCss': 'p { margin: 0; }',
#
#     },
# }
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [["Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker"],
                    ['NumberedList', 'BulletedList', "Indent", "Outdent", 'JustifyLeft', 'JustifyCenter',
                     'JustifyRight', 'JustifyBlock'],
                    ["Image", "Table", "Link", "Unlink", "Anchor", "SectionLink", "Subscript", "Superscript"],
                    ['Undo', 'Redo'], ["Source"],
                    ["Maximize"]],
        'contentsCss': 'p { margin: 0; }',
    },
}
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'full',
#          'extraPlugins': ','.join([
#             'uploadimage', # the upload image feature
#             # your extra plugins here
#             'div',
#             'autolink',
#             'autoembed',
#             'embedsemantic',
#             'autogrow',
#             # 'devtools',
#             'widget',
#             'lineutils',
#             'clipboard',
#             'dialog',
#             'dialogui',
#             'elementspath'
#         ]),
#
#     },
# }
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR,'coolsite_cache')
    }
}
# *** Settings ***
#     TAGGIT_AUTOSUGGEST_STATIC_BASE_URL:
#         Instead of collecting and serving the static files directly, you can
#         also set this variable to your static base URL somewhere else.
#     TAGGIT_AUTOSUGGEST_MAX_SUGGESTIONS (Defaults to 20):
#         The amount of suggestions is limited, you can raise or lower the limit
#         of default 20 using this setting.
# *** Settings ***
# TAGGIT_AUTOSUGGEST_STATIC_BASE_URL:
#         Instead of collecting and serving the static files directly, you can
#         also set this variable to your static base URL somewhere else.
#     TAGGIT_AUTOSUGGEST_MAX_SUGGESTIONS (Defaults to 20):
#         The amount of suggestions is limited, you can raise or lower the limit
#         of default 20 using this setting.
#     TAGGIT_AUTOSUGGEST_CSS_FILENAME (Defaults to 'autoSuggest.css'):
#         Set the CSS file which best fits your site elements.
#             The CSS file have to be in 'jquery-autosuggest/css/'.
#     TAGGIT_AUTOSUGGEST_MODELS (Defaults to tuple('taggit','Tag'))
#         The Tag model used, if you happen to use Taggit custom tagging.
TAGGIT_AUTOSUGGEST_MODELS = [
    'taggit.Tag',  # Ensure default Tag model is there just in case.
    # 'photos.People',
]
# django_heroku.settings(locals())