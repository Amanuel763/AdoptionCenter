from django.contrib import admin
from .models import Adopt
from django.utils.html import format_html

# Register your models here.

class AdoptAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px"; />'.format(object.pet_photo.url))

    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'pet_title', 'city', 'state', 'breed')
    list_display_links = ('id', 'thumbnail', 'pet_title')
    search_fields = ('id', 'pet_title', 'state')
    list_filter = ('city', 'state', 'breed')

admin.site.register(Adopt, AdoptAdmin)