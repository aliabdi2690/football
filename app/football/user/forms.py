from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUsermodel


class SignUpForm(UserCreationForm):
    date_of_birth = forms.DateField(required=True)
    class Meta:
        model = MyUsermodel
        fields = ('username', 'email', 'password1', 'password2', 'date_of_birth')

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput())


