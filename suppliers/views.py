from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.contrib import messages
from django.urls import reverse
from .logic.logic_supplier import get_suppliers, create_supplier
from .forms import SupplierForm
from suppliers.models import Supplier
from antusu_experimento1.auth0backend import getRole
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
# def supplier_list(request):
#     role = getRole(request)
#     if role == "gerente":
#         suppliers = get_suppliers()
#         qs_json = serializers.serialize('json', suppliers)
#         return HttpResponse(qs_json, content_type='application/json')
#     else:
#         return HttpResponse("Unauthorized User")

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
