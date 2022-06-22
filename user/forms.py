
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from dishes.models import *
from settings.models import *


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={"type":"text", "value":"", "class":"input main-input-box","name":"username", "id":"username"}),
            'first_name': forms.TextInput(attrs={"type":"text", "value":"", "class":"input main-input-box","name":"first_name", "id":"first_name"}),
            'last_name': forms.TextInput(attrs={"type":"text", "value":"", "class":"input main-input-box","name":"email", "id":"email"}),
            'email': forms.TextInput(attrs={"type":"email", "value":"", "class":"input main-input-box","name":"first_name", "id":"first_name"}),
            'password1': forms.TextInput(attrs={'class':'input main-input-box'})
        }
        


