from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

# Create your views here.
def home(request):
    #return HttpResponse("Teste <strong>MAIN</strong>")
    return render(request=request,
                  template_name="main/inicio.html")
                  #,context={"Pessoas": Pessoa.objects.all})