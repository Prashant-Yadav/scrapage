#admin_scraper

from django.contrib import admin

# Register your models here.
from .models import Webpage, ScrapWebpage

admin.site.register(Webpage)
admin.site.register(ScrapWebpage)
