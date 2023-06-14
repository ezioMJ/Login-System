from django import forms

class Login(forms.Form):
    email = forms.EmailField(label="Email ID")
    password = forms.CharField(label="Password",widget=forms.PasswordInput())

class Signup(forms.Form):
    email = forms.EmailField(label="Email ID")
    pass1 = forms.CharField(label="Password",widget=forms.PasswordInput())
    pass2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput())

class User(forms.Form):
    name = forms.CharField(label="Name")
    age = forms.IntegerField(label="Age")
    gender = forms.CharField(label="Gender")
    phone = forms.CharField(label="Phone No")
    country = forms.CharField(label="Country")