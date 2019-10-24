from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) #자동로그인
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {'form':form,}
    return render(request, 'accounts/signup.html',context)

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

def logout(request):
    auth_logout(request)
    return redirect('articles:index')
