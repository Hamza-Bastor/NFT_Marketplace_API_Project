from dataclasses import fields
from django.forms import ModelForm
from .models import Register
from django import forms


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = "__all__"

        labels = {
            'username': '',
            'address': '',
            'password': '',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'userIdInput', 'placeholder': 'Username'}),
            'address': forms.EmailInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Email address'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'floatingPassword', 'placeholder': 'Password'}),
        }
