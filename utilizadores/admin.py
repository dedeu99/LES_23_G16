from django.contrib import admin
from .models import Pessoa,Docente,Funcionario
# Register your models here.
admin.site.register(Pessoa)

admin.site.register(Docente)

admin.site.register(Funcionario)