from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import *
from django.template import loader




# Create your views here.

"""def curso(self):
    curso = Curso(nombre="Desarrollo Web", cursada = "19881")
    curso.save()
    Documento = f"--->Curso: {curso.nombre} Cursada: {curso.cursada}"

    return HttpResponse(Documento)"""
def inicio (request):
    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)


def curso (request):
    cursos = Curso.objects.all()    
    plantilla = loader.get_template('cursos.html')
   
    documento = plantilla.render({"curso":cursos})
    
    return HttpResponse(documento)

def estudiante (request):
    estudiantes = Estudiante.objects.all()    
    plantilla = loader.get_template('estudiantes.html')
   
    documento = plantilla.render({"estudiante":estudiantes})
    
    return HttpResponse(documento)

def profesor (request):
    profesores = Porfesor.objects.all()    
    plantilla = loader.get_template('profesores.html')
   
    documento = plantilla.render({"profesor":profesores})
    
    return HttpResponse(documento)

def entregable (request):
    entregables = Entregable.objects.all()    
    plantilla = loader.get_template('entregables.html')
   
    documento = plantilla.render({"entregables":entregables})
    
    return HttpResponse(documento)
