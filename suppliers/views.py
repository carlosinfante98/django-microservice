from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core import serializers
from django.contrib import messages
from django.urls import reverse
from .logic.logic_supplier import get_suppliers, create_supplier
from .forms import SupplierForm
from suppliers.models import Supplier
from antusu_experimento1.auth0backend import getRole
from django.contrib.auth.decorators import login_required
from django.conf import settings
import requests
import json

@login_required
def supplier_list(request):
    role = getRole(request)
    if role == "gerente" or role == "admin":
        suppliers = get_suppliers()
        context = {
            'supplier_list': suppliers
        }
        return render(request, 'suppliers/suppliers.html', context)
    else:
        return HttpResponse("Unauthorized User")

def supplier_detail(request, supplier_id):
    try:
        supplier = Supplier.objects.get(pk=supplier_id)
        r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
        shoes = r.json()
        list = [obj for obj in shoes if obj['supplier'] == int(supplier_id)]
    except supplier.DoesNotExist:
        return HttpResponseNotFound("ERROR")  
    context = {
        'sup': supplier,
        'shoes': list,
    }
    return render(request, 'suppliers/supplier_detail.html', context)


def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            create_supplier(form)
            messages.add_message(request, messages.SUCCESS,
                                 'Supplier created successfully')
            return HttpResponseRedirect(reverse('supplier_new'))
        else:
            print(form.errors)
    else:
        form = SupplierForm()

    context = {
        'form': form,
    }
    return render(request, 'suppliers/supplier_form.html', context)
