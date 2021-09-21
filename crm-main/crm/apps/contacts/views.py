from django.shortcuts import render

from apps.companies.models import Companies
from apps.contacts.forms import ContactsForm
from apps.contacts.models import Contacts


def clients_all(request):
    clients = Contacts.objects.all()
    return render(request, 'common/clients.html', {'clients': clients})


def add_client(request):
    if request.POST:
        form = ContactsForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            contacts = {'first_name': data.get('first_name', ''),
                        'last_name': data.get('last_name', ''),
                        'phone': data.get('phone', ''),
                        'email': data.get('email', ''),
                        'position': data.get('position', ''),
                        'company': Companies.objects.get(id=data.get('company', '')),
                        'sex':  data.get('sex', ''),
                        'profile_image': data.get('profile_image', '')
                        }
            contacts = Contacts(**contacts)
            contacts.save()

            clients = Contacts.objects.all()
            return render(request, 'common/clients.html', {'clients': clients})
    companies = Companies.objects.all()
    return render(request, 'common/create_client.html', {'companies': companies})
