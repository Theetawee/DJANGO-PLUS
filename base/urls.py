from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from base.sitemaps import StaticViewSitemap
from django.views.generic.base import TemplateView


sitemaps={
    # 'accounts':AccountSitemap,
    'others':StaticViewSitemap
}


urlpatterns = [
    path("robots.txt",TemplateView.as_view(template_name="base/robots.txt", content_type="text/plain")),
    path('admin/', admin.site.urls),     
    path('',include('main.urls')),
    path('accounts/',include('accounts.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
    urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns  += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'main.views.custom_404_view'
handler400 = 'main.views.custom_404_view'
handler500 = 'main.views.custom_500_view'
handler403 = 'main.views.custom_404_view'

admin.site.site_header='App name'
admin.site.site_title='App Admin'
admin.site.index_title='Welcome to the Admin Panel'