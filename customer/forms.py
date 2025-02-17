from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class CustomerRegisterForm(UserCreationForm):
    email = forms.EmailField()
    address = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=20)

    class Meta:
        model = Customer
        fields = ['username', 'email', 'address', 'phone', 'password1', 'password2']