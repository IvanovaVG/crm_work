from django import forms


class CompaniesForms(forms.Form):
    name = forms.CharField(max_length=200)
    sphere = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)