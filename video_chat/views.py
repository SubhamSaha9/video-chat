from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from .middleware import *
from django.views.decorators.cache import never_cache
from .creds import appID, serverSecret

# Create your views here.
@guest
def index(request):
    return render(request, 'index.html')

@guest
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'auth/login.html', {'success': "Registration successful. Please login."})
        else:
            error_message = form.errors.as_text()
            return render(request, 'auth/signup.html', {'error': error_message})

    return render(request, 'auth/signup.html')

@guest
def login_view(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard")
        else:
            return render(request, 'auth/login.html', {'error': "Invalid credentials. Please try again."})

    return render(request, 'auth/login.html')

@never_cache
@auth
def dashboard(request):
    return render(request, 'dashboard/dashboard.html', {'name': request.user.first_name})


@auth
def videocall(request):
    return render(request, 'dashboard/videocall.html', {'name': request.user.first_name + " " + request.user.last_name, "appID": appID, "serverSecret": serverSecret})


@auth
def logout_view(request):
    logout(request)
    return redirect("/login")


@auth
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'dashboard/joinroom.html')
