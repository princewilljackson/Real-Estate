from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import bedroom_choices, state_choices

from .models import Sale, Rent

def sales(request):
  sales = Sale.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(sales, 6)
  page = request.GET.get('page')
  paged_sales = paginator.get_page(page)

  context = {
    'sales': paged_sales
  }

  return render(request, 'listings/sales.html', context)

def rents(request):
  rents = Rent.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(rents, 6)
  page = request.GET.get('page')
  paged_rents = paginator.get_page(page)

  context = {
    'rents': paged_rents
  }

  return render(request, 'listings/rents.html', context)

def sale(request, sale_id):
  sale = get_object_or_404(Sale, pk=sale_id)
  
  context = {
    'sale': sale
  }

  return render(request, 'listings/sale.html', context)
  
def rent(request, rent_id):
  rent = get_object_or_404(Rent, pk=rent_id)

  context = {
    'rent': rent
  }

  return render(request, 'listings/rent.html', context)

def search(request):
  queryset_list = Sale.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)

  context = {
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'sales': queryset_list,
    'values': request.GET
  }

  return render(request, 'listings/search.html', context)