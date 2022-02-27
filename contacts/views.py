import email
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.

def inquiry(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', 'default value')
        last_name = request.POST.get('last_name', 'default value')
        customer_need = request.POST.get('customer_need', 'default value')
        city = request.POST.get('city', 'default value')
        state = request.POST.get('state', 'default value')
        email = request.POST.get('email', 'default value')
        phone = request.POST.get('phone', 'default value')
        message = request.POST.get('message', 'default value')
        contact = Contact(first_name=first_name, last_name=last_name, customer_need=customer_need, city=city, state=state, email=email, phone=phone, message=message)


        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            'New inquiry for a Dog',
            'You have a new inquiry about a dog. Please Login to your admin panel.',
            'greuther76@gmail.com',
            [admin_email],
            fail_silently=False,
        )




        contact.save()
        messages.success(request, 'Your request has been submited')
        return redirect('/')

        