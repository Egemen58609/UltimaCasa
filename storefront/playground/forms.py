from django import forms
from .models import Gebruiker, Bieding, Home,status,Role

class Memberform(forms.ModelForm):
    class Meta:
        model = Gebruiker
        fields = ["username", 'email', 'password', ]

class Memberform1(forms.ModelForm):
    class Meta:
        model = Gebruiker
        fields = ["username", 'email', ]

class Memberform2(forms.ModelForm):
    class Meta:
        model = Gebruiker
        fields = ["username", 'email', 'role' ]

class HuisForm(forms.ModelForm):
    class Meta:
        model = Bieding
        fields = ["bod"]

class Biedingform(forms.ModelForm):
    class Meta:
        model = Bieding
        fields = '__all__'

class Statusform(forms.ModelForm):
    class Meta:
        model = status
        fields = ['status', 'statuscode']

class Huisform1(forms.Form):
    datum = forms.DateField()
    gebruiker = forms.CharField()
    straat = forms.CharField()
    plaats = forms.CharField()
    postcode = forms.CharField()

class Rolform(forms.ModelForm):
    class Meta:
        model = Role
        fields = ["naam", "waarde"]

class Homeform(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['datum', 'straat', 'postcode', 'plaats']  