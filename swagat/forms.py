from django import forms 

class LoginForm(forms.Form):
    username=forms.CharField(label='Username',max_length=30)
    password=forms.CharField(label='Password',max_length=30,widget=forms.PasswordInput)
class RegisterForm(forms.Form):
    username=forms.CharField(label='Username',max_length=30)
    password=forms.CharField(label='Password',max_length=30,widget=forms.PasswordInput)
    email=forms.CharField(label='Email',max_length=30,widget=forms.EmailInput)