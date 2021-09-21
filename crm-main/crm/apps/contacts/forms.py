from django import forms


class ContactsForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=20)
    position = forms.CharField(max_length=30)
    company = forms.CharField(max_length=30)
    sex = forms.CharField(max_length=20)
    profile_image = forms.ImageField()
