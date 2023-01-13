from django import forms



class ClientsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.IntegerField()
    address = forms.CharField(max_length=100)
