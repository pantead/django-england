from typing import Reversible
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeDoneView
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from accounts.forms import NewUserForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserChangeForm,PasswordChangeForm, UserCreationForm
# from django.contrib.auth import authenticate, update_session_auth_hash
# from django.contrib.auth.decorators import login_required


def home(request):
    numbers = [1,2,3,4,5]
    name = 'max'
    
    args = {'myName': name,'numbers':numbers}
    return render(request, 'accounts/home.html',args)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account')
    else:
        form = UserCreationForm()
        args = {'form':form}
        return render(request,'accounts/register.html',args)


def view_profile(request):
    args ={'user':request.user}
    return render(request,'accounts/profile.html',args)  


def edit_profile(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')
        
    else: 
        form = PasswordChangeDoneView(instance=request.user)
        args={'form':form}
        return render(request,'accounts/edit_profile.html')


def edit_profile(request):
    if request.method == 'POST':
        form = PasswordChangeDoneView(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
        
    else: 
        form = PasswordChangeDoneView(instance=request.user)
        args={'form':form}
        return render(request,'accounts/change_password.html',args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(Reversible('accounts:view_profile'))
        else:
            return redirect(Reversible('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)