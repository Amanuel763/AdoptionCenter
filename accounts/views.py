from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username", "default value")
        password = request.POST.get("password", "default value")

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        firstname=request.POST.get("first_name", "default value")
        lastname=request.POST.get("first_name", "default value")
        username = request.POST.get("username", "default value")
        email = request.POST.get("email", "default value")
        password = request.POST.get("password", "default value")
        confirm_password = request.POST.get("confirm_password", "default value")

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in.')
                    return redirect('home')
                    user.save()
                    messages.success(request, 'You are registered successfully.')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You have logged out!')
        return redirect('home')
    return redirect('home')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')