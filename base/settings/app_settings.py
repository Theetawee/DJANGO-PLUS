import os

# Determines whether the admin site is enabled
IS_ADMIN_ENABLED = os.environ.get("IS_ADMIN_ENABLED", "False").lower() == "true"

# Defines the URL path for the admin site if it is enabled
ADMIN_SITE_URL_PATH = os.environ.get("ADMIN_SITE_URL_PATH", "admin")


IS_PWA_ENABLED = os.environ.get("IS_PWA_ENABLED", "False").lower() == "true"

APP_NAME = "Platform"

DARK_MODE = os.environ.get("DARK_MODE", "True").lower() == "true"
