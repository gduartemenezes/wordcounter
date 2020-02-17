

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('count/', views.count, name ='count'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
