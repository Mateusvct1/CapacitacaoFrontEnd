from django.shortcuts import render
from .models import Person

def person_list(request):
    persons = Person.objects.all()
# Obtém todos os objetos da classe Person do banco de dados
    return render(request, 'person.html', {'persons': Person})
# Renderiza o template 'person.html'
