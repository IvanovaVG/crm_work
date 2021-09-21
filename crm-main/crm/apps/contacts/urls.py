from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.clients_all, name='clients'),
    path('add_client/', views.add_client, name='add_client'),
]
