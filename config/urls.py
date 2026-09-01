from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from django.views.generic import TemplateView
from website.sitemaps import StaticViewSitemap
from website.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt', TemplateView.as_view(
        template_name='robots.txt',
        content_type='text/plain'
    )),
    path('sitemap.xml', sitemap, {
        'sitemaps': {'static': StaticViewSitemap},
    }),
    path('', home, name='home'),
]
