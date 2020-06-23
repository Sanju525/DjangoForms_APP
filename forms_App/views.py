from django.shortcuts import render
# from forms_App import forms
from . import forms
from forms_App.models import UserLogs

# Create your views here.

# Landing Page
def index(request):
    return render(request, 'forms_App/index.html', {})


# Signup Page
def signup(request):
    form = forms.Register()

    if request.method == 'POST':
        user_form = forms.Register(request.POST)
        if user_form.is_valid():
            print(user_form.cleaned_data['username'])

    return render(request, 'forms_App/signup.html', {'form': form})


# Login Page
def Login(request):
    formLogin = forms.LOGIN()

    if request.method == 'POST':
        user_form = forms.LOGIN(request.POST)

        if user_form.is_valid():
            print(user_form.cleaned_data['username'])
    else:
        print("no")
    return render(request, 'forms_App/Login.html', {'form': formLogin})
