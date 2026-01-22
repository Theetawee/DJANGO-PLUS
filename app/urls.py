from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

api_version = "v1"

urlpatterns = [
    path(f"{api_version}/", include("main.urls")),
    path(f"{api_version}/accounts/", include("accounts.urls")),
    path(f"{api_version}/auth/", include("dj_waanverse_auth.urls")),
]

if settings.IS_ADMIN_ENABLED:
    urlpatterns += [
        path(
            f"{settings.ADMIN_SITE_URL_PATH}/",
            admin.site.urls,
        )
    ]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = "The Chat"
admin.site.site_title = "The Chat Admin"
admin.site.index_title = "Welcome to the Admin Panel"
