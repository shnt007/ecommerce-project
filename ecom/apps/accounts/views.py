import email
from multiprocessing import context
from re import template
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from traitlets import Instance
from .models import Profile
from django.urls import reverse
# Create your views here.


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


def user_profile(request, id):
    user_obj = User.objects.get(id=id)
    context = {
        'user_obj': user_obj
    }

    return render(request, 'accounts/profile.html', context)


def user_edit(request, id):
    user_obj = User.objects.get(id=id)
    context = {"db_data": user_obj}
    if request.method == 'POST':
        user_obj.first_name = request.POST.get('first_name')
        user_obj.last_name = request.POST.get('last_name')
        user_obj.email = request.POST.get('email')
        user_obj.save()
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
