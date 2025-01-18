from django.shortcuts import redirect

def auth(function):
    def wrapper(request):
        if request.user.is_authenticated:
            return function(request)
        return redirect("login")
    return wrapper


def guest(function):
    def wrapper(request):
        if request.user.is_authenticated:
            return redirect("dashboard")
        return function(request)
    return wrapper