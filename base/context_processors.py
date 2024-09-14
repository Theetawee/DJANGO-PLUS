from django.conf import settings


def is_pwa_enabled(request):

    return {
        "is_pwa_enabled": settings.IS_PWA_ENABLED,
        "APP_NAME": settings.APP_NAME,
        "dark_mode": settings.DARK_MODE,
    }
