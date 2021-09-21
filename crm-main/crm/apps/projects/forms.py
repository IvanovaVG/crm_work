from django import forms


class ProjectForms(forms.Form):
    name = forms.CharField(max_length=250)
    description = forms.CharField(max_length=1000)
    company = forms.CharField(max_length=250)



class ProjectChangeForms(forms.Form):
    name = forms.CharField(max_length=250)
    description = forms.CharField(max_length=1000)
