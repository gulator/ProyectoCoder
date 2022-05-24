from django.urls import path
from . import views


urlpatterns = [
    
    path('cursos/', views.curso),
    path('estudiantes/', views.estudiante),
    path('profesores/', views.profesor),
    path('entregables/', views.entregable)
]