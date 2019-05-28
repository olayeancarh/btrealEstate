from django.contrib import admin

from .models import *

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('title', 'is_published', 'price', 'list_date', 'realtor')
    list_editable = ('is_published',)
    search_fields = ('title', 'is_published', 'price', 'list_date', 'realtor__name')
    list_per_page = 25
admin.site.register(Listing, ListingAdmin)
