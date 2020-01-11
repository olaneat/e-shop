from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150, help_text='enter a valid mail address')
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    state = forms.CharField(max_length=150)
    location = forms.CharField(widget=forms.TextInput)
    phone_number =forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 
                    'last_name', 'phone_number', 'location', 'state', 
        ]
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length= 150)
    password = forms.CharField(widget=forms.PasswordInput, max_length= 150)    