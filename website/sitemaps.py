from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = "weekly"

    def items(self):
        return [
            "home",
            "private_chef_nairobi",
            "private_chef_kenya",
            "catering_nairobi",
            "fine_dining_nairobi",
            "wedding_catering_nairobi",
            "cooking_classes_nairobi",
            "baking_classes_nairobi",
            "chef_network_nairobi",
        ]

    def location(self, item):
        return reverse(item)
