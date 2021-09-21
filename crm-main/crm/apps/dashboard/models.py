from django.db import models
from django.contrib.auth.models import User

from apps.contacts.models import Contacts
from apps.projects.models import Projects


class Tasks(models.Model):
    status_choice = [
        ('New', 'new'),
        ('InProgress', 'in progress'),
        ('Done', 'done'),
    ]
    priority_status = [
        ('LP', 'low priority'),
        ('MP', 'medium priority'),
        ('HP', 'high priority'),
    ]
    type_task = [
        ('Software', 'software'),
        ('Information', 'information'),
        ('Consulting', 'consulting'),
        ('Product', 'product'),
    ]
    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=status_choice,
        default='New',
    )
    executor = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)
    priority = models.CharField(max_length=20,
                                choices=priority_status,
                                default='LP',
                                )
    type_task = models.CharField(max_length=20,
                                 choices=type_task,
                                 default='',
                                 )
    date_crate = models.DateField(auto_now_add=True)
    dead_line = models.DateField()
    coast = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    #creted_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='id')
    customer = models.ForeignKey(Contacts, on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Projects, on_delete=models.DO_NOTHING, default='', null=True, blank=True)

    def __str__(self):
        return self.name
