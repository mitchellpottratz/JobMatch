import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY')

# SECRET_KEY = 'myjq#w4rmci3e#ebxh*!g(3b)s#k38jv4$zo+yb^bwdapar5@1'

    

ALLOWED_HOSTS = ['job-matching.herokuapp.com', '127.0.0.1']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # my apps
    'users.apps.UsersConfig',
    'company_users.apps.CompanyUsersConfig',
    'candidate_users.apps.CandidateUsersConfig',
    'company_account.apps.CompanyAccountConfig',
    'candidate_account.apps.CandidateAccountConfig',
    'job_posts.apps.JobPostsConfig',
    'skills.apps.SkillsConfig',
    'projects.apps.ProjectsConfig',
    'experience.apps.ExperienceConfig',
    'matches.apps.MatchesConfig',

    # installed packages
    'location_field.apps.DefaultConfig',
    'phone_field',
    'tinymce', # text editor
    'debug_toolbar', # for testing performance
    'storages',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# required to list ip address by django_toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]


ROOT_URLCONF = 'JobMatch.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'JobMatch/templates')],
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


WSGI_APPLICATION = 'JobMatch.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# production database configuration
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# configures static folder to load css, js and images
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Extra lookup directories for collectstatic to find static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#  configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# configures folder for storing images
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# tells django where to look for the user model
AUTH_USER_MODEL = 'users.User'


# configuration for tinymce text editor
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True


# Amazon s3 configuration
AWS_ACCESS_KEY_ID = 'AKIAUN2ZCZZEAX36TBWC'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'job-match'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

# arn:aws:s3:::job-match

DEFAULT_FILE_STORAGE = 'JobMatch.storage_backends.MediaStorage'







