from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.companies.models import Companies


class Contacts(models.Model):
    sex_choose = [
        ('M', 'male'),
        ('F', 'female'),
        ('O', 'other'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    position = models.CharField(max_length=30)
    company = models.ForeignKey(Companies, on_delete=models.DO_NOTHING)
    #country = models.CharField(max_length=10)
    sex = models.CharField(max_length=20,
                           choices=sex_choose,
                           default='',
                           )
    profile_image = models.ImageField(default='default-avatar.png', upload_to='clients/', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.position}'

    # @receiver(post_save, sender=Contacts)
    # def save_user_profile(sender, instance, **kwargs):
    #     try:
    #         instance.profile.save()
    #     except ObjectDoesNotExist:
    #         Contacts.objects.create(user=instance)
