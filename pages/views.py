from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import bedroom_choices, state_choices

from listings.models import Sale, Rent
from realtors.models import Realtor

def index(request):
    sales = Sale.objects.order_by('-list_date').filter(is_published=True)[:3]
    rents = Rent.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'sales': sales,
        'rents': rents,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)