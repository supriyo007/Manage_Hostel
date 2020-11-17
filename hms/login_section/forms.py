from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email=forms.EmailField(max_length=200, help_text='Email is Required')
    dob=forms.DateField(help_text='Format: YYYY-MM-DD')
    class Meta:
        model=User
        fields=('username','email','dob','password1','password2',)
