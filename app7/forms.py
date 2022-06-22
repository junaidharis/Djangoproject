
from dataclasses import fields
from pyexpat import model
from .models import Register
from django import forms
class RegisterForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8)
    class Meta():
        model= Register
        fields= '__all__'
class LoginForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput, max_length=8)
    class Meta ():
        model = Register
        fields = ("Email", "Password")
            
    

        