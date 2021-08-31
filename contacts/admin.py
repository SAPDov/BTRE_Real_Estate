from django.contrib import admin
from .models import Contacts

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'inquiry_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'listing', 'email')
    list_per_page = 20


admin.site.register(Contacts, ContactAdmin)