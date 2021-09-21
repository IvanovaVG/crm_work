from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.companies_all, name='companies'),
    path('create_company/', views.create_company, name='create_company'),
    path('change_company/<int:id>', views.change_company, name='change_company'),
]
