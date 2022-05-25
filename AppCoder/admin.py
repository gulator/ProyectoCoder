from django.contrib import admin
from AppCoder.views import profesor
from .models import *

# Register your models here.
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Porfesor)
admin.site.register(Entregable)