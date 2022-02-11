from django.shortcuts import render
from .models import Team
# Create your views here.

def home(request):
    teams = Team.objects.all()

    data = {
        'teams': teams
    }

    return render(request, 'pages/home.html', data)

def contact(request):
    return render(request, 'pages/contact.html')


def blog(request):
    return render(request, 'pages/blog.html')


def login(request):
    return render(request, 'pages/login.html')


def register(request):
    return render(request, 'pages/register  .html')