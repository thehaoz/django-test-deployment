from django import forms
from django.contrib.auth.models import User
from password.models import UserProfile
### django.contrib.auth.models import user
### User Class contains
### Username, first_name, last_name, email, password....



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ("username", "email", "password")
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('portfolio_site', 'profile_pic')
