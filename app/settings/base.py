import os
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY")

AUTH_USER_MODEL = "accounts.Account"


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts",
    "rest_framework",
    "main",
    "dj_waanverse_auth",
    "debug_toolbar",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_USER", "t3Uw2@example.com")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD", "password123")
EMAIL_USE_TLS = True


REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "app.utils.CustomPageNumberPagination",
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "dj_waanverse_auth.authentication.JWTAuthentication",
    ),
    "PAGE_SIZE": 10,
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}


WAANVERSE_AUTH_CONFIG = {
    "BASIC_ACCOUNT_SERIALIZER": "accounts.serializers.BasicAccountSerializer",
    "PLATFORM_NAME": "11th Shelf",
    "ENABLE_ADMIN_PANEL": True,
    "ACCESS_TOKEN_COOKIE_NAME": "a_t",
    "REFRESH_TOKEN_COOKIE_NAME": "r_t",
    "IS_TESTING": True,
    "REFRESH_TOKEN_COOKIE_MAX_AGE": timedelta(days=30),
    "ACCESS_TOKEN_COOKIE_MAX_AGE": timedelta(minutes=30),
}


CORS_ALLOW_CREDENTIALS = True


IS_ADMIN_ENABLED = os.environ.get("IS_ADMIN_ENABLED", "True").lower() == "true"

ADMIN_SITE_URL_PATH = os.environ.get("ADMIN_SITE_URL_PATH", "admin")
