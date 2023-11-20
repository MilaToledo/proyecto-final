from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view_inicio(request):
    return HttpResponse("que onda?")

def view_cursos(request):
    #return HttpResponse("cursos")
    return render(request, "AppCoder/padre.html")