from base.settings.base import *

DEBUG = False

ALLOWED_HOSTS = [""]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("PGDATABASE"),
        "USER": os.environ.get("PGUSER"),
        "PASSWORD": os.environ.get("PGPASSWORD"),
        "HOST": os.environ.get("PGHOST"),
        "PORT": os.environ.get("PGPORT", 5432),
        "OPTIONS": {
            "sslmode": "require",
        },
    }
}

STATIC_URL = "https://your_cdn_url/"

BACKUP_DIRECTORY = os.path.join(BASE_DIR, "backups/production")

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
CSRF_COOKIE_SECURE = True
