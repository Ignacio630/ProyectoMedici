from django import forms

class ProvidersForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.IntegerField()
    address = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)