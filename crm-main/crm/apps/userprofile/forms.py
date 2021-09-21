from django.contrib.auth.models import User
from django.forms import ModelForm

from apps.userprofile.models import Profile


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'phone_number', 'birth_date', 'profile_image')
