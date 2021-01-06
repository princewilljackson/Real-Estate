from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import SaleContact, RentContact

def sale_contact(request):
  if request.method == 'POST':
    sale_id = request.POST['sale_id']
    sale = request.POST['sale']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = SaleContact.objects.all().filter(sale_id=sale_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this listing')
        return redirect('listings:sale', sale_id=sale_id)

    sale_contact = SaleContact(sale=sale, sale_id=sale_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    sale_contact.save()

    # Send email
    # send_mail(
    #   'Property Listing Inquiry',
    #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
    #   'traversy.brad@gmail.com',
    #   [realtor_email, 'techguyinfo@gmail.com'],
    #   fail_silently=False
    # )

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('listings:sale', sale_id=sale_id)


def rent_contact(request):
  if request.method == 'POST':
    rent_id = request.POST['rent_id']
    rent = request.POST['rent']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = RentContact.objects.all().filter(rent_id=rent_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this listing')
        return redirect('listings:rent', rent_id=rent_id)

    rent_contact = RentContact(rent=rent, rent_id=rent_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    rent_contact.save()

    # Send email
    # send_mail(
    #   'Property Listing Inquiry',
    #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
    #   'traversy.brad@gmail.com',
    #   [realtor_email, 'techguyinfo@gmail.com'],
    #   fail_silently=False
    # )

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('listings:rent', rent_id=rent_id)