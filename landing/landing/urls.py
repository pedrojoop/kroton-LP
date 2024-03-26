"""
URL configuration for landing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import TemplateView
from django.contrib import admin
from . import views

urlpatterns = [
    path('buscar_cursos/', views.buscar_cursos, name='buscar_cursos'),
    path('obter_cidades/', views.obter_cidades, name='obter_cidades'),
    path('obter_estados/', views.obter_estados, name='obter_estados'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),  # Servir index.html como a página inicial
    path('admin/', admin.site.urls),  # Rota para o painel de administração do Django
]

