from django.contrib import admin

from .models import Sale, Rent

admin.site.site_header = 'JAYCEE & JAY LTD'
admin.site.site_title = 'JAYCEE & JAY LTD'
admin.site.index_title = 'WELCOME TO JAYCEE & JAY LTD ADMIN DASHBOARD'

class SaleAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'state', 'list_date', 'realtor', 'sold')
  list_display_links = ('id', 'title')
  list_filter = ('realtor',)
  list_editable = ('is_published', 'sold')
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
  list_per_page = 25

admin.site.register(Sale, SaleAdmin)

class RentAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'state', 'list_date', 'realtor', 'occupied')
  list_display_links = ('id', 'title')
  list_filter = ('realtor',)
  list_editable = ('is_published', 'occupied')
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
  list_per_page = 25

admin.site.register(Rent, RentAdmin)