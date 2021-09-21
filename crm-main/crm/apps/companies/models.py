from django.db import models


class Spheres(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Companies(models.Model):
    sphere_choose = [
        ('IT', 'IT'),
        ('Banks', 'Banks'),
        ('Logistic', 'Logistic'),
    ]
    name = models.CharField(max_length=200)
    sphere = models.CharField(max_length=100,
                           choices=sphere_choose,
                           default='',
                           )
    description = models.TextField(max_length=500)
    email = models.EmailField()
    #representative = models.ForeignKey(Contacts, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.name
