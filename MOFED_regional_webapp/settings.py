
import os
from pathlib import Path
from django.contrib.admin.options import ModelAdmin as DEFAULT_MODEL_ADMIN

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vl1osx-&@rl##2ogt%^kv$dri#h)tppm8)&5qg1f+i233$g$2$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'kanenus.com','www.kanenus.com', '127.0.0.1', '*']
CSRF_COOKIE_SECURE = True
# Application definition


INSTALLED_APPS = [
   
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'about_us',
    'documents',
    'news',
    'suppliers',
    'vacancies',
    'dashboard',
    'task_manager',
    'blogs',
    'accounts',
    'templatetags',
    'core',
    # 'jazzmin',
    'djangocms_admin_style',
    'modeltranslation', # dynamic translation
    'django.contrib.admin',
     
    # cms
    "django.contrib.sites",
    "cms",
    "menus",
    "treebeard",
    
    "sekizai",
    'djangocms_alias',
    # 'djangocms_versioning',
    
    'filer',
    'easy_thumbnails',
    'djangocms_text_ckeditor',
    "djangocms_frontend",
    "djangocms_frontend.contrib.accordion",
    "djangocms_frontend.contrib.alert",
    "djangocms_frontend.contrib.badge",
    "djangocms_frontend.contrib.card",
    "djangocms_frontend.contrib.carousel",
    "djangocms_frontend.contrib.collapse",
    "djangocms_frontend.contrib.content",
    "djangocms_frontend.contrib.grid",
    "djangocms_frontend.contrib.image",
    "djangocms_frontend.contrib.jumbotron",
    "djangocms_frontend.contrib.link",
    "djangocms_frontend.contrib.listgroup",
    "djangocms_frontend.contrib.media",
    "djangocms_frontend.contrib.tabs",
    "djangocms_frontend.contrib.utilities",

    "djangocms_file",
    "djangocms_picture",
    "djangocms_video",
    "djangocms_googlemap",
    "djangocms_snippet",
    "djangocms_style",
    
    # translation
    # "parler",  
    'rosetta',
    
    


  
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'core.middleware.VisitorMiddleware',

    # cms
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    
]

ROOT_URLCONF = 'MOFED_regional_webapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.recent_news_mega',
                'core.context_processors.stgs',
                'core.context_processors.search_result',
                 # cms
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                
            ],
        },
    },
]


THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
WSGI_APPLICATION = 'MOFED_regional_webapp.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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


LANGUAGE_CODE = 'en'



LANGUAGES = (
    ('en', ('English')),
    ('es', ('Spanish')),
    ('tx', ('Tigrigna')),
    ('ax', ('Amharic')),

)

LANGS = {
    'en':'English',
    'ax':'Amharic',
    'tx':'Tigrigna'

}
# implement the search field for filer 
DEFAULT_MODEL_ADMIN.search_fields = ['']


# Our custom languages used in Ethiopia, not defined by Django
EXTRA_LANG_INFO = {
    'ax': {
        'bidi': False, # right-to-left
        'code': 'ax',
        'name': 'አማርኛ',
        'name_local': u'አማርኛ',
    },
    'tx': {
        'bidi': False, # right-to-left
        'code': 'tx',
        'name': 'ትግርኛ',
        'name_local': u'ትግርኛ',
    },
    
}

# Add custom languages not provided by Django
import django.conf.locale
LANG_INFO = dict(django.conf.locale.LANG_INFO, **EXTRA_LANG_INFO)
django.conf.locale.LANG_INFO = LANG_INFO


LOCALE_PATHS = [
    os.path.join(BASE_DIR,'locale'),
]


TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_THOUSAND_SEPARATOR = True

USE_TZ = True

GRAPH_MODELS ={
    'all_applications': True,
    'graph_models': True,
    }

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [BASE_DIR, "static"]

#media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# settings.py

AUTH_USER_MODEL = 'accounts.UserProfile'

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER='compacct01@gmail.com'
EMAIL_FROM ='Yismu'
EMAIL_HOST_PASSWORD='qxnwvesqfznyozbw'
EMAIL_USE_TLS=True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'



# cms settings
SITE_ID = 1

CMS_TEMPLATES = (
    ("front/cms_base.html", ("Cms Base Template")),
)

# Enable permissions
# https://docs.django-cms.org/en/release-4.1.x/topics/permissions.html

CMS_PERMISSION = True

CMS_CONFIRM_VERSION4 = True

# Allow admin sidebar to open admin URLs

X_FRAME_OPTIONS = 'SAMEORIGIN'

# Enable inline editing with djangocms-text-ckeditor
# https://github.com/django-cms/djangocms-text-ckeditor#inline-editing-feature

TEXT_INLINE_EDITING = True

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)


INTERNAL_IPS = [
    "127.0.0.1",
]

DJANGOCMS_VERSIONING_ALLOW_DELETING_VERSIONS = True

# roseta settings
ROSETTA_MESSAGES_PER_PAGE = 50

# parler settings
PARLER_DEFAULT_LANGUAGE_CODE = 'en'
# PARLER_LANGUAGES = {
#     None: (
#         {'code': 'en',},
#         {'code': 'ax',},
#         {'code': 'tx',},
#     ),
#     'default': {
#         'fallbacks': ['en'],          # defaults to PARLER_DEFAULT_LANGUAGE_CODE
#         'hide_untranslated': False,   # the default; let .active_translations() return fallbacks too.
#     }
# }

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_LANGUAGES = ('en', 'ax', 'tx')

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Finance Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Admin",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Admin",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "static/front/imgs/logo_south.jpg",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "static/front/imgs/lg.jpg",

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Welcome to Southern Ethiopia Finance Bureau ",

    # Copyright on the footer
    "copyright": "Acme Library Ltd",
    "extra_css": ["static/front/css/custom_admin.css"],

    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string 
    "search_model": ["suppliers.Supplier"],

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,

    ############
    # Top Menu #
    ############

  
}

CORS_ORIGIN_ALLOW_ALL = True
CSP_MIDDLEWARE = [
    'csp.middleware.CSPMiddleware',
    # Other middleware classes...
]

CSP_DEFAULT_SRC = ("'self'",)  # Allow resources from the same origin

# Allow embedding from specific domains
CSP_FRAME_SRC = ("'self'",)

X_FRAME_OPTIONS = 'SAMEORIGIN'  # Allow embedding from the same origin