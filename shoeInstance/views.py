from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib import messages
from django.core import serializers

from shoeInstance.models import ShoeInstance
from .forms import ShoeInstanceForm
from .logic.logic_shoeInstance import get_all_shoeInstances, create_shoeInstance
# Create your views here.

def shoeI_list(request):
  shoes = get_all_shoeInstances()
  qs_json = serializers.serialize('json', shoes)
  return HttpResponse(qs_json, content_type='application/json')

def shoe_create(request):
  if request.method == 'POST':
    form =  ShoeInstanceForm(request.POST)
    if form.is_valid():
      create_shoeInstance(form)
      messages.add_message(request, messages.SUCCESS, 'Shoe Instance created successfully')
      return HttpResponseRedirect(reverse('shoeI_new'))
    else:
      print(form.errors)
  else:
    form = ShoeInstanceForm()
  
  context = {
    'form': form,
  }
  return render(request, 'shoeInstance/shoeI_form.html', context)
  