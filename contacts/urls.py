from django.urls import path

from . import views

app_name = 'contacts'

urlpatterns = [
  path('sale_contact/', views.sale_contact, name='sale_contact'),
  path('rent_contact/', views.rent_contact, name='rent_contact')
]