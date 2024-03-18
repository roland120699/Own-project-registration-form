from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=30, label='Username')
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')