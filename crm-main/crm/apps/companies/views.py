from django.shortcuts import render, redirect

from apps.companies.forms import CompaniesForms
from apps.companies.models import Companies


def companies_all(request):
    companies = Companies.objects.all()
    return render(request, 'common/companies.html', {'companies': companies})


def create_company(request):
    if request.POST:
        form = CompaniesForms(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            company = {'name': data.get('name', ''),
                       'sphere': data.get('sphere', ''),
                       'description': data.get('description', ''),
                       'email': data.get('email', ''),
                       }
            company = Companies(**company)
            company.save()
            companies = Companies.objects.all()
            return render(request, 'common/companies.html', {'companies': companies})

    return render(request, 'common/create_company.html')


def change_company(request, id):
    if request.POST:
        form = CompaniesForms(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            companies = Companies.objects.get(id=id)
            if companies.name != data.get('name', ''):
                companies.name = data.get('name', '')
            if companies.sphere != data.get('sphere', ''):
                companies.sphere = data.get('sphere', '')
            if companies.description != data.get('description', ''):
                companies.description = data.get('description', '')
            if companies.email != data.get('email', ''):
                companies.email = data.get('email', '')
            companies.save()
            companies = Companies.objects.all()
            return render(request, 'common/companies.html', {'companies': companies})
    company = Companies.objects.get(id=id)
    return render(request, 'common/change_company.html',  {'company': company})
