from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
  # path('', views.index, name='index')
    path('', views.purchase_list, name = 'purchase_list'),
    path('new', csrf_exempt(views.purchase_create), name='purchase_new'),
    path('delete/<int:id>', views.purchase_delete, name='purchase_delete'),
]