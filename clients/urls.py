from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
  # path('', views.index, name='index')
    path('', views.clients_list, name = 'client_list'),
    path('new', csrf_exempt(views.clients_create), name='clients_new'),
]