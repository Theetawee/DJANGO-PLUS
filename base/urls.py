from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.views.generic.base import TemplateView

from base.sitemap import StaticViewSitemap
from base.utils import manifest, offline, service_worker

sitemaps = {"others": StaticViewSitemap}


urlpatterns = [
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="base/robots.txt", content_type="text/plain"
        ),
    ),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]


urlpatterns += i18n_patterns(
    path("", include("main.urls")),
    path("accounts/", include("accounts.urls")),
    prefix_default_language=True,
)


if settings.IS_PWA_ENABLED:
    urlpatterns += [
        re_path(r"^serviceworker\.js$", service_worker, name="sw"),
        re_path(r"^manifest\.json$", manifest, name="manifest"),
        path("offline/", offline, name="offline"),
    ]

if settings.IS_ADMIN_ENABLED:
    urlpatterns += [path(f"{settings.ADMIN_SITE_URL_PATH}/", admin.site.urls)]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = "base.utils.custom_404_view"
handler400 = "base.utils.custom_404_view"
handler500 = "base.utils.custom_500_view"
handler403 = "base.utils.custom_404_view"

admin.site.site_header = f"{settings.APP_NAME}"
admin.site.site_title = f"{settings.APP_NAME} Admin"
admin.site.index_title = "Welcome to the Admin Panel"
