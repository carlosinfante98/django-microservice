from django.contrib import admin
from django.urls import include, path
from .views import home_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', home_view, name='index'),
    path('shoes/', include('shoe.urls')),
    path('admin/', admin.site.urls),
    path('purchases/', include('purchase.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('clients/', include('clients.urls')),
    path(r'', include('django.contrib.auth.urls')),
    path(r'', include('social_django.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)