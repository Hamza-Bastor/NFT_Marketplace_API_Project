from dataclasses import fields
from tkinter import Widget
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'type': 'text',
            'class': 'form-control',
            'id': 'username',
            'placeholder': 'username',
        })
        self.fields["email"].widget.attrs.update({
            'type': 'email',
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'name@example.com',
        })
        self.fields["password1"].widget.attrs.update({
            'type': 'password',
            'class': 'form-control',
            'id': 'password1',
            'placeholder': 'Password',
        })
        self.fields["password2"].widget.attrs.update({
            'type': 'password',
            'class': 'form-control',
            'id': 'password2',
            'placeholder': 'Password',
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
