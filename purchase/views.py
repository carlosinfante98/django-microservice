from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib import messages
from django.core import serializers

from purchase.models import Purchase
from .forms import PurchaseForm
from .logic.logic_purchase import get_purchases, create_purchase

# Create your views here.

def purchase_create(request):
  if request.method == 'POST':
    form =  PurchaseForm(request.POST)
    if form.is_valid():
      create_purchase(form)
      messages.add_message(request, messages.SUCCESS, 'Purchase created successfully')
      return HttpResponseRedirect(reverse('purchase_new'))
    else:
      print(form.errors)
  else:
    form = PurchaseForm()
  
  context = {
    'form': form,
  }
  return render(request, 'purchase/purchase_form.html', context)

def purchase_list(request):
  purchases = get_purchases()
  qs_json = serializers.serialize('json', purchases)
  return HttpResponse(qs_json, content_type='application/json')
  
def purchase_delete(request, id):
  purchase = Purchase.objects.get(id=id)
  purchase.delete()
  return redirect('purchase_list')
