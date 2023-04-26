"""
Django settings for news project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

APPS_DIR = BASE_DIR / 'apps'
sys.path.insert(0, str(APPS_DIR))

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x79phzc$g974xomf-)6&nof$80-b)jtj7*idh*(ks7ewmhwh&+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'charts',
    'posts',
    'comments',
    # 'panel',
    'users',
    # 'martor',
    # 'qr_code',
    'bootstrap5',
    'home',
    'fontawesomefree',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'news.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'news.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

STATICFILES_DIRS = [
    BASE_DIR / 'resources'
]

# CKEDITOR
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_RESTRICT_BY_DATE = True
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_FORCE_JPEG_COMPRESSION = True
CKEDITOR_JPEG_COMPRESSION_QUALITY = 90
CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_CONFIGS = {
    'default': {
        'height': 'auto',
        'width': 'auto',
    }
}

JAZZMIN_SETTINGS = {
    "site_title": "财有料-后台管理系统",
    "site_header": "财有料-管理系统",
    "site_brand": "财有料",
    "site_logo": "/front/images/icons/logo.png",
    "welcome_sign": "欢迎使用财有料管理系统",
    "copyright": "财有料",
    "search_model": ["users.User", "posts.Post"],
    "user_avatar": None,
    "dark_mode_theme": "darkly",
    "topmenu_links": [
        {"name": "首页", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "users.User"},
        {"name": "组", "url": "admin:auth_group_changelist", "permissions": ["auth.view_group"]},
        {"name": "文章", "url": "admin:posts_post_changelist", "permissions": ["posts.view_post"]},
        {"name": "评论", "url": "admin:comments_comment_changelist", "permissions": ["comments.view_comment"]},
        {"name": "分类", "url": "admin:posts_category_changelist", "permissions": ["posts.view_category"]},
        {"name": "退出", "url": "home", "icon": "fas fa-sign-out-alt"},
    ],
}
