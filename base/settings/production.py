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

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "WARNING",  # Display warnings and above in the console
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "mail_admins": {
            "level": "WARNING",  # Send warnings and errors to admins via email
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "formatters": {
        "simple": {
            "format": "[{asctime}] {levelname} {message}",
            "style": "{",
        },
    },
    "loggers": {
        "django": {
            "handlers": [
                "console",
                "mail_admins",
            ],  # Send logs to both console and admins
            "level": "WARNING",  # Set to warning level and above
            "propagate": True,
        },
        "django.request": {
            "handlers": ["mail_admins"],  # Critical request errors go to admins
            "level": "ERROR",  # Only log errors for requests
            "propagate": False,
        },
    },
}

ADMINS = [
    ("Tawee", "tawee@waanverse.com"),
]

STATIC_URL = "https://your_cdn_url/"

BACKUP_DIRECTORY = os.path.join(BASE_DIR, "backups/production")

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
CSRF_COOKIE_SECURE = True
