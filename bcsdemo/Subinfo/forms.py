from django import forms

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class RegisterForm(forms.Form):
    user=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 're-password'}))
   # subject = forms.ChoiceField(choices=STATES)


class LoginForm(forms.Form):
    user = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
