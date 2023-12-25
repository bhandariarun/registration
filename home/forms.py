# myapp/forms.py
from django import forms
#from phonenumber_field.formfields import PhoneNumberField

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.Form):
    fname = forms.CharField(max_length=100)
    mname = forms.CharField(max_length=100)
    lname = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100)
    cpassword = forms.CharField(max_length = 100)
