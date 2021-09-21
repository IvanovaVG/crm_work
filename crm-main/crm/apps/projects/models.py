from django.db import models

from apps.companies.models import Companies


class Projects(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    company = models.ForeignKey(Companies, on_delete=models.DO_NOTHING, default=None)
    date_crate = models.DateField(auto_now_add=True)

