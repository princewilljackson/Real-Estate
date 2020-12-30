from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='sales'),
    path('<int:sale_id>', views.sale, name='sale'),
    path('search', views.search, name='search'),
]