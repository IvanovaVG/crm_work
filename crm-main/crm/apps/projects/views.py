from django.shortcuts import render

from .forms import ProjectForms, ProjectChangeForms
from .models import Projects
from django.contrib.auth.mixins import LoginRequiredMixin

from ..companies.models import Companies
from ..dashboard.models import Tasks


def projects_all(request):
    projects = Projects.objects.all()
    tasks = Tasks.objects.all()
    return render(request, 'common/projects.html', {'projects': projects, 'tasks': tasks})


def projects_add(request):
    if request.POST:
        form = ProjectForms(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            project = {'name': data.get('name', ''),
                       'description': data.get('description', ''),
                       'company': Companies.objects.get(id=data.get('company', '')),
                       }
            project = Projects(**project)
            project.save()
            projects = Projects.objects.all()
            return render(request, 'common/projects.html', {'projects': projects})
    companies = Companies.objects.all()
    return render(request, 'common/create_project.html', {'companies': companies})


def projects_change(request, id):
    if request.POST:
        form = ProjectChangeForms(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            projects = Projects.objects.get(id=id)
            if projects.name != data.get('name', ''):
                projects.name = data.get('name', '')
            if projects.description != data.get('description', ''):
                projects.description = data.get('description', '')
            projects.save()
            projects = Projects.objects.all()
            return render(request, 'common/projects.html', {'projects': projects})
    project = Projects.objects.get(id=id)
    return render(request, 'common/change_project.html', {'project': project})
