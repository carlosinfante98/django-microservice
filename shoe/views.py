from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib import messages
from django.core import serializers
from django.template import loader
from shoe.models import Shoe
from .forms import ShoeForm
from .logic.logic_shoe import get_shoes, create_shoe
# Create your views here.


# def shoe_list(request):
#     shoes = get_shoes()
#     qs_json = serializers.serialize('json', shoes)
#     return HttpResponse(qs_json, content_type='application/json')

def shoe_list(request):
    shoes = get_shoes()
    context = {
        'shoes_list': shoes
    }
    return render(request, 'shoe/shoes.html', context)

def shoe_create(request):
    if request.method == 'POST':
        form = ShoeForm(request.POST)
        if form.is_valid():
            create_shoe(form)
            messages.add_message(request, messages.SUCCESS,
                                 'Shoe created successfully')
            return HttpResponseRedirect(reverse('shoe_new'))
        else:
            print(form.errors)
    else:
        form = ShoeForm()

    context = {
        'form': form,
    }
    return render(request, 'shoe/shoe_form.html', context)


def shoe_delete(request, id):
    shoe = Shoe.objects.get(id=id)
    shoe.delete()
    return redirect('index')


# def shoe_list(req):
#  return HttpResponse("<h1>Shoe shoe_list</h1>")
