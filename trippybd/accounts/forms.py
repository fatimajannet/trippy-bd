from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    email       = forms.EmailField(required=True)
    fname       = forms.CharField(max_length=50,  label="First Name")
    mname       = forms.CharField(max_length=50,  label="Middle Name", required=False)
    lname       = forms.CharField(max_length=50,  label="Last Name")
    u_location  = forms.CharField(max_length=255, label="Location", required=False)

    class Meta:
        model  = User
        fields = [
            'username', 'email',
            'fname', 'mname', 'lname',
            'u_location',
            'password1', 'password2'
        ]


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = [
            'username', 'email',
            'fname', 'mname', 'lname',
            'u_location'
        ]
        labels = {
            'fname':      'First Name',
            'mname':      'Middle Name',
            'lname':      'Last Name',
            'u_location': 'Location',
        }