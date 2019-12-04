from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
  path('', views.supplier_list, name='supplier_list'),
  path('new', csrf_exempt(views.supplier_create), name='supplier_new'),
  path('<supplier_id>', views.supplier_detail),
]