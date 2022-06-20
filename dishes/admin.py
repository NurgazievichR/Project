from django.contrib import admin

from dishes.models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url':('title',)}
    fields = ['title', 'image', ('icon', 'icon2'), 'url']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url':('title',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url':('title',)}
   
