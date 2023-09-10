from django.urls import path, re_path
from .views import index,service_worker,manifest,offline,robots,sitemap


urlpatterns=[
    path('',index,name='home'),
    re_path(r'^serviceworker\.js$', service_worker, name='sw'),
    re_path(r'^manifest\.json$', manifest, name='manifest'),
    path('offline/',offline,name='offline'),
    path('sitemap/',sitemap,name='sitemap'),
    re_path(r'^robots\.txt$', robots, name='robots'),
]