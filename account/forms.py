from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import FarmerProfile


class UserRegistrationForm(forms.ModelForm):

    # Require user to enter password twice and check that they are the same.
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:

        # Info is used in from user model
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'email',)

        # Add bootstrap form-control class to built in forms for styling
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

        }


class FarmerProfileEditForm(forms.ModelForm):
    class Meta:
        model = FarmerProfile
        fields = ('street', 'city', 'state', 'zipcode', 'farm_name',
                  'farm_description', 'farm_products', 'farm_photo', 'status')
        widgets = {
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'farm_name': forms.TextInput(attrs={'class': 'form-control'}),
            'farm_description': forms.Textarea(attrs={'class': 'form-control'}),
            'farm_products': forms.Textarea(attrs={'class': 'form-control'}),
            'farm_photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),

        }


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label="Username", max_length=30,
        widget=forms.TextInput(attrs={
            "class": 'form-control', "type": "text", "id": "username"
        }))
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control", "id": "password"
        }))
