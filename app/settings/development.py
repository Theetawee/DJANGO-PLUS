# flake8: noqa
from app.settings.base import *  # noqa: F403
from datetime import timedelta

# from base.settings.hosts_settings import *

DEBUG = True

ALLOWED_HOSTS = ["*"]


STATIC_URL = "static/"
MEDIA_URL = "media/"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # noqa: F405
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),  # noqa: F405
    os.path.join(BASE_DIR, "media"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn")

MEDIA_ROOT = os.path.join(BASE_DIR, "media_cdn")

INTERNAL_IPS = [
    "127.0.0.1",
]

BACKUP_DIRECTORY = os.path.join(BASE_DIR, "backups/development")
SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = False

CORS_ALLOW_ALL_ORIGINS = True

DEFAULT_FROM_EMAIL = "noreply@waanverse.com"
DEFAULT_FROM_NAME = "11th Shelf"


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [
    "rest_framework.renderers.JSONRenderer",
    "rest_framework.renderers.BrowsableAPIRenderer",
]


WAANVERSE_AUTH_CONFIG["PUBLIC_KEY_PATH"] = os.path.join(
    BASE_DIR, "secrets", "public_key.pem"
)
WAANVERSE_AUTH_CONFIG["PRIVATE_KEY_PATH"] = os.path.join(
    BASE_DIR, "secrets", "private_key.pem"
)


WAANVERSE_AUTH_CONFIG["COOKIE_DOMAIN"] = "localhost"
WAANVERSE_AUTH_CONFIG["COOKIE_SECURE"] = False
WAANVERSE_AUTH_CONFIG["COOKIE_SAMESITE_POLICY"] = "Lax"
WAANVERSE_AUTH_CONFIG["ACCESS_TOKEN_COOKIE_MAX_AGE"] = timedelta(minutes=15)
WAANVERSE_AUTH_CONFIG["REFRESH_TOKEN_COOKIE_MAX_AGE"] = timedelta(days=30)
WAANVERSE_AUTH_CONFIG["COOKIE_HTTP_ONLY"] = False


SITE_URL = "http://localhost:8001"
