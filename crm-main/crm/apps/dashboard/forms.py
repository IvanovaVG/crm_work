from django import forms


class TaskForm(forms.Form):
    name = forms.CharField(max_length=100)
    status = forms.CharField(max_length=20)
    executor = forms.CharField(max_length=100)
    priority = forms.CharField(max_length=100)
    type_task = forms.CharField(max_length=100)
    dead_line = forms.DateField()
    coast = forms.CharField(max_length=100)
    project = forms.CharField(max_length=100)
    customer = forms.CharField(max_length=100)


class StatusForm(forms.Form):
    status = forms.CharField(max_length=20)
