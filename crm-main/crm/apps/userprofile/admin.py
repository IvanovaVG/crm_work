from django.contrib import admin
from .models import Profile
from ..companies.models import Spheres, Companies
from ..contacts.models import Contacts
from ..dashboard.models import Tasks
from ..projects.models import Projects

admin.site.register(Profile)
admin.site.register(Tasks)
admin.site.register(Contacts)
admin.site.register(Spheres)
admin.site.register(Companies)
admin.site.register(Projects)