from django.contrib import admin
from .models import Cliente,Vendedor,Servicos
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Servicos)