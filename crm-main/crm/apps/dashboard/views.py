from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Tasks
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskForm, StatusForm
from ..contacts.models import Contacts
from ..projects.models import Projects


def tasks_all(request):
    tasks = Tasks.objects.all()
    return render(request, 'common/dashboard.html', {'tasks': tasks})


def tasks_person(request):
    print(request)
    tasks = Tasks.objects.filter(executor=1)
    return render(request, 'common/tasks.html', {'tasks': tasks})


def add_task(request):
    tasks = Tasks.objects.all()
    projects = Projects.objects.all()
    executors = User.objects.all()
    priority = {'LP': 'low priority',
                'MP': 'medium priority',
                'HP': 'high priority'}
    type_tasks = {'Software': 'software',
                  'Information': 'information',
                  'Consulting': 'consulting',
                  'Product': 'product'}

    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tasks = {'name': data.get('name', ''),
                     'status': data.get('status', 'New'),
                     'priority': data.get('priority', ''),
                     'type_task': data.get('type_task', ''),
                     'dead_line': datetime.strptime(str(data.get('dead_line', '')), '%Y-%m-%d'),
                     'coast': data.get('coast', ''),
                     'customer': Contacts.objects.get(id=data.get('customer', '')),
                     'project': Projects.objects.get(id=data.get('project', '')),
                     'executor': User.objects.get(id=data.get('executor', ''))
                     }
            task = Tasks(**tasks)
            task.save()
            tasks = Tasks.objects.all()
            return render(request, 'common/dashboard.html', {'tasks': tasks})
    customers = Contacts.objects.all()
    tasks = Tasks.objects.filter(executor=request.user.id)
    return render(request, 'common/create_task.html',
                  {'tasks': tasks, 'projects': projects, 'executors': executors, 'priority': priority,
                   'type_tasks': type_tasks, 'customers': customers})


def change_status(request, id):
    task = Tasks.objects.get(id=id)
    if request.POST:
        form = StatusForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if task.status != data.get('status', 'New'):
                task.status = data.get('status', 'New')
            task.save()
            tasks = Tasks.objects.all()
            return render(request, 'common/dashboard.html', {'tasks': tasks})

    task = Tasks.objects.get(id=id)
    return render(request, 'common/change_status.html', {'task': task})
