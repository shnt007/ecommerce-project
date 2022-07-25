import email
from multiprocessing import context
from re import template
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile
from django.urls import reverse
# Create your views here.


# def profile(request):
#     template = 'accounts/profile.html'
#     context = {
#         'user': User.objects.get(email)
#     }
#     return render(request, template, context)


def user_profile(request, id):
    if request.method == "POST":
        user_obj = User.objects.get(id=id)
        form = Profile
        formSave = Profile(request.POST, request.FILES)
        if formSave.is_valid():
            formSave.save()
            return render(request, 'accounts/profile.html', {'form': form, 'data': user_obj})
        else:
            return render(request, 'accounts/profile.html', {'form': form, 'data': user_obj})
    else:
        user_obj = User
        return render(request, 'accounts/profile.html', {'form': user_obj})


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)

        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username=email, password=password)
        if user_obj:
            login(request, user_obj)
            # return reverse('accounts/profile.html', kwargs={'id': email})
            return render(request, 'accounts/profile.html')

        messages.success(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)
    return render(request, 'accounts/account.html')


def user_register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)

        if user_obj.exists():
            messages.warning(request, 'Email already exits.!')
            return HttpResponseRedirect(request.path_info)

        user_obj = User.objects.create(
            first_name=first_name, last_name=last_name, email=email,  username=email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/account.html')


# def user_profile(request, username):
#     db_data = Profile.objects.get(id=username)
#     context = {
#         "db_data": db_data
#     }
#     return render(request, 'accounts/profile.html', context)


def user_edit(request, username):
    db_data = Profile.object.get(id=username)
    context = {
        "db_data": db_data
    }
    if request.method == 'POST':
        db_data.first_name = request.POST.get('first_name')
        db_data.Last_name = request.POST.get('last_name')
        db_data.contact = request.POST.get("contact")
        db_data.email = request.POST.get("email")
        db_data.password = request.POST.get("password")
        db_data.save()
        return render(request, 'accounts/profile.html', context)
    else:
        return render(request, 'accounts/edit.html', context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def activate_email(request, email_token):
    try:
        user = Profile.objects.get(email_token=email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token.')
