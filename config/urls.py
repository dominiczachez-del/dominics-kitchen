from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from django.views.generic import TemplateView

from website.sitemaps import StaticViewSitemap
from website.views import (
    home,
    private_chef_nairobi,
    private_chef_kenya,
    catering_nairobi,
    fine_dining_nairobi,
    wedding_catering_nairobi,
    cooking_classes_nairobi,
    baking_classes_nairobi,
    chef_network_nairobi,
)


sitemaps = {
    "static": StaticViewSitemap,
}


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain",
        ),
        name="robots",
    ),

    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="sitemap",
    ),

    path("", home, name="home"),

    path(
        "private-chef-nairobi/",
        private_chef_nairobi,
        name="private_chef_nairobi",
    ),

    path(
        "private-chef-kenya/",
        private_chef_kenya,
        name="private_chef_kenya",
    ),

    path(
        "catering-nairobi/",
        catering_nairobi,
        name="catering_nairobi",
    ),

    path(
        "fine-dining-nairobi/",
        fine_dining_nairobi,
        name="fine_dining_nairobi",
    ),

    path(
        "wedding-catering-nairobi/",
        wedding_catering_nairobi,
        name="wedding_catering_nairobi",
    ),

    path(
        "cooking-classes-nairobi/",
        cooking_classes_nairobi,
        name="cooking_classes_nairobi",
    ),

    path(
        "baking-classes-nairobi/",
        baking_classes_nairobi,
        name="baking_classes_nairobi",
    ),

    path(
        "private-chef-network-nairobi/",
        chef_network_nairobi,
        name="chef_network_nairobi",
    ),
]
