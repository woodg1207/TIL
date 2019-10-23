from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from IPython import embed
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.views.decorators.http import require_POST
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Create your views here.
def signup(request):
    # user 가 인증된 상태면 안들어가 지도록
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            #form.save()를 통해 반환된 User 클래스의 인스턴스를
            # auth_login의 인자로 전달
            #회워가입후 자동으로 로그인 되어진다. 
            user = form.save()

            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {'form':form, }
    return render(request, 'accounts/auth_form.html', context)

def login(request):
     # user 가 인증된 상태면 안들어가 지도록
    if request.user.is_authenticated:
        return redirect('articles:index')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {'form':form, }
    return render(request, 'accounts/auth_form.html', context)


def logout(request):
    # user.delete()  회원 자체 삭제
    auth_logout(request)
    return redirect('articles:index')

@require_POST
def delete(request):
    request.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance= request.user)
    context = {'form':form, }
    return render(request, 'accounts/auth_form.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        # data보다 user가 먼저 들어감
        form = PasswordChangeForm(request.user, request.POST) 
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form,}
    return render(request, 'accounts/auth_form.html', context)

def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    # html에서 with 구문을 사용하면 조회를 하는 횟수가 줄어든다. markdown 참조
    articles = person.article_set.all() # 역참조
    comments = person.comment_set.all()
    context = {'person': person,'articles': articles, 'comments':comments,}
    return render(request, 'accounts/profile.html', context)

