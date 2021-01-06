from django.urls import path

from . import views

app_name = 'listings'

urlpatterns = [
    path('rent/<int:rent_id>/', views.rent, name='rent'),
    path('sale/<int:sale_id>/', views.sale, name='sale'),
    path('rents/', views.rents, name='rents'),
    path('sales/', views.sales, name='sales'),
    path('search/', views.search, name='search'),
]