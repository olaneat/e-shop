from django.shortcuts import render, redirect, HttpResponse
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate
# Create your views here.

def signUp(request):
    if request.method == 'POST':
        signupform = SignUpForm(request.POST)
        if signupform.is_valid():
            signupform.save()
            username =signupform.cleaned_data.get('username')
            raw_password = signupform.cleaned_data.get('password1')
            user = authenticate(username =username, password=raw_password)
            login(request, user)
            return redirect('catlog:index')
    else:
        signupform = SignUpForm()
    return render(request, 'registration/signup.html', {'signupform': signupform})


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request, username=cd['username'], password = cd['password'])    
            login(request, user)
            return redirect('catlog:index')
        else:
            return HttpResponse('invalid login detail')
    else:
        login_form = LoginForm()
    return render(request, 'registration/login.html', {'login_form': login_form})

