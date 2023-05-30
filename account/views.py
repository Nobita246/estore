from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import Profile


# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_obj = User.objects.filter(username=email)
        if not user_obj.exists():
            messages.warning(request, "Please Check Username.")
            return HttpResponseRedirect(request.path_info)

        login_user = authenticate(username=email, password=password)
        if login_user:
            return HttpResponseRedirect("/home")

        messages.success(request, "Email has been sent.")

    return render(request, "account/login.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_obj = User.objects.filter(username=email)
        if user_obj.exists():
            messages.warning(request, "This Email is already used.")
            return HttpResponseRedirect(request.path_info)

        new_user = User.objects.create(
            first_name=first_name, last_name=last_name, username=email
        )
        new_user.set_password(password)
        new_user.save()
        messages.success(request, "Email has been sent.")

    return render(request, "account/register.html")


def activate_user(request, email_token):
    try:
        user = Profile.objects.get(email_token=email_token)
        user.is_email_verified = True
        user.save()
        messages.success(request, "Your Email Has been verified.")

        return HttpResponseRedirect("/account/login")

    except Exception as e:
        print(e)
