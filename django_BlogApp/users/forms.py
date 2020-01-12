from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Define meta class
    # Meta class tells which django model should receive the data from this form
    # It also controls the fields to be displayed on the form and the order
    # in which these fields are displayed

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
