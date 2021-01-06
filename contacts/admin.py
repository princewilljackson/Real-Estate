from django.contrib import admin

from .models import SaleContact, RentContact, PropertyManagement

class SaleContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'sale', 'email', 'contact_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email', 'sale')
  list_per_page = 25

admin.site.register(SaleContact, SaleContactAdmin)

class RentContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'rent', 'email', 'contact_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email', 'rent')
  list_per_page = 25

admin.site.register(RentContact, RentContactAdmin)

class PropertyManagementAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email', 'context')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email')
  list_per_page = 25

admin.site.register(PropertyManagement, PropertyManagementAdmin)