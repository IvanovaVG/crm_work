from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.tasks_all, name='dashboard'),
    path('tasks/', views.tasks_person, name='tasks'),
    path('add_task/', views.add_task, name='add_task'),
    path('change_status/<int:id>', views.change_status, name='change_status'),
]