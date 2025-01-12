from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

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

