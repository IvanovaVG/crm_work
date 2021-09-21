from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.projects_all, name='projects'),
    path('projects_add/', views.projects_add, name='projects_add'),
    path('projects_change/<int:id>', views.projects_change, name='projects_change'),

]