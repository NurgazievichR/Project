
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from dishes.models import *
from settings.models import *


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        


