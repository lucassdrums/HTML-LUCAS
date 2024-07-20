from django.shortcuts import render
from django.http import HttpResponse


#def index(request):
    #return HttpResponse("<h1>Olá Mundo !!!</h1><h2>Ola</h2>")


def index(request):
    return render(request, "index.html")
