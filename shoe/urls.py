from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from shoeInstance import views as shoeI_Views

urlpatterns = [
  # path('', views.index, name='index')
    path('', views.shoe_list, name = 'index'),
    path('new', csrf_exempt(views.shoe_create), name='shoe_new'),
    path('delete/<int:id>', views.shoe_delete, name='shoe_delete'),
    path('shoeInstance/', shoeI_Views.shoeI_list, name= 'index'),
    path('shoeInstance/new', shoeI_Views.shoe_create, name= 'shoeI_new')
]