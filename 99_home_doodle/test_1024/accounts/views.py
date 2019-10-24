from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Create your views here.
def signup(request):
    # if request.user.is_authenticated:
    #     return redirect('articles:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {'form':form, }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request == 'POST':
        pass
    else:
        form = AuthenticationForm()
    context = {'form':form,}
    return render(request, 'accounts/login.html', context)
