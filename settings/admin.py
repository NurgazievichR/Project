from django.contrib import admin

from settings.models import *


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    fields = [('network','amount'),'address']
    list_display = ['network', 'address']
    list_display_links = ['network', 'address']

admin.site.register(Advertisement)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'description', 'image']


