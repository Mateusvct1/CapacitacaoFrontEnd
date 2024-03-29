"""
URL configuration for projetodjango project.

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
#Importa as funções
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import hello
from .views import receber_dados
from .views import ler
# Inicia uma lista chamada que define os padrões de URL da aplicação
urlpatterns = [
    path('hello/', hello),
    path('receber_dados/', receber_dados, name='receber_dados'),
    path('ler/', ler),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Adiciona as configurações de URL para servir arquivos de mídia durante o desenvolvimento
