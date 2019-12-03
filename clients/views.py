from django.shortcuts import render # To visualize in webpage
from .forms import ClientForm # To be able to get user input.
from .logic.logic_client import * # Imports all the logic of the corresponding class.
from django.contrib import messages #???
from django.core import serializers # To manage JSON returns for the requests
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse #To be able to redirect to other urls

# Create your views here.
def clients_create(request):
    if request.method == 'POST':
        form =  ClientForm(request.POST)
        if form.is_valid():
            create_client(form)
            messages.add_message(request, messages.SUCCESS, 'Client created successfully')
            return HttpResponseRedirect(reverse('clients_new'))
        else:
            print(form.errors)
    else:
        form = ClientForm()
    
    context = {
        'form': form,
    }
    return render(request, 'clients/clients_form.html', context)



def clients_list(request):
    clients = get_clients()
    qs_json = serializers.serialize('json', clients)
    return HttpResponse(qs_json, content_type='application/json')