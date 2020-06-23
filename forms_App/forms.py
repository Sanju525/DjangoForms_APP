from django import forms


class Register(forms.Form):
    username = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class LOGIN(forms.Form):
    username = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
