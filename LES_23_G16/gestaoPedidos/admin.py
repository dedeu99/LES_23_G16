from django.contrib import admin

# Register your models here.
from .models import Pedido, Pessoa

admin.site.register(Pedido)
admin.site.register(Pessoa)   
