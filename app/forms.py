from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class rgisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=50, required=True)
    last_name=forms.CharField(max_length=50, required=True)
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

class update_profile(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
        ]