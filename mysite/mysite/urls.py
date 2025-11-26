
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),# 1 muestra las urls de la app accounts
    path('accounts/',include('django.contrib.auth.urls')), # 2 vistas login, logout
    path('',TemplateView.as_view(template_name='home.html'),name='home'), #3 vista home
]
