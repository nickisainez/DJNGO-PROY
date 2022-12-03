from django.contrib import admin

from myapp.models import Alumno,Salon,Person,Cliente,Vendedor,Evaluacion,Examenfinal,Proyecto,ProyectoProxy,Profesor

admin.site.register(Alumno)
admin.site.register(Salon)
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Examenfinal)
admin.site.register(Proyecto)
admin.site.register(ProyectoProxy)
admin.site.register(Profesor)
