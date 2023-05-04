from django import forms


class RegisterForm(forms.Form):
    user = forms.CharField(max_length=32)
    password1 = forms.CharField(widget=forms.PasswordInput(), min_length=3)
    password2 = forms.CharField(widget=forms.PasswordInput(), min_length=3)


class LoginForm(forms.Form):
    user = forms.CharField(max_length=32)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=3)
