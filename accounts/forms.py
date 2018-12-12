from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    company_name = forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    street_address = forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    apartment_number = forms.CharField(max_length=254, required=False, widget=forms.TextInput())
    city = forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    state = forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    zipcode = forms.CharField(max_length=5, required=True, widget=forms.TextInput())
    class Meta:
        model = User
        fields = ('company_name', 'username', 'email', 'street_address', 'apartment_number', 'city', 'state', 'zipcode', 'password1', 'password2')
