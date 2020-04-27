from django import forms

class LoginForm(froms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    