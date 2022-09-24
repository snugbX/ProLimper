"""ProLimper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from cliente.views import home, cad_Cliente, cad_Vendedor, cad_Servico, update_Servico, delete_Servico
from cliente.views import update_Cliente, delete_Cliente, delete_Vendedor, update_Vendedor , PDF_Servicos2, HTML_Servicos_PDF
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('HTML_Servicos_PDF/<int:pk>/', HTML_Servicos_PDF, name='HTML_Servicos_PDF'),
    path('Novo_cliente/', cad_Cliente, name='cad_Cliente'),
    path('Novo_vendedor/', cad_Vendedor, name='cad_Vendedor'),
    path('Novo_servico/', cad_Servico, name='cad_Servico'),

    #path('PDF_Servicos/<int:pk>/', PDF_Servicos.as_view(), name='GeraPDF_Servico'),
    path('PDF_Servicos/<int:pk>/', PDF_Servicos2, name='GeraPDF_Servico'),
    path('Update_servico/<int:pk>/', update_Servico, name='up_Servico'),
    path('Deletar_servico/<int:pk>/', delete_Servico.as_view(), name='del_Servico'),

    path('Update_cliente/<int:pk>/', update_Cliente, name='up_Cliente'),
    path('Deletar_cliente/<int:pk>/', delete_Cliente.as_view(), name='del_Cliente'),

    path('Update_vendedor/<int:pk>/', update_Vendedor, name='up_Vendedor'),
    path('Deletar_vendedor/<int:pk>/', delete_Vendedor.as_view(), name='del_Vendedor'),



]

urlpatterns += staticfiles_urlpatterns()
