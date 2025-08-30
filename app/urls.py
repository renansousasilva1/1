from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from base.sitemaps import StaticViewSitemap  # << corrigi aqui

sitemaps = {
    'static': StaticViewSitemap,
    # no futuro você pode adicionar outros, ex: 'posts': PostSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
]
