from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_date')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    


# Register your models here.   
admin.site.register(Contact, ContactAdmin)