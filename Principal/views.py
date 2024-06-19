from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Programa  
from .models import Instructores
from .models import Profesionales
from .models import Miembros 
from .models import Consultas
from .forms import formulario_miembro
from .forms import formularioinstructor
from .forms import formularioprograma

# Create your views here.

def inicio(req):
        return render(req,"inicio.html", {})

def programa(req):
        return render(req,"programa.html", {})

def instructores(req):
       return render(req,"instructores.html", {})

def profesionales(req):
       return render(req,"profesionales.html", {})

def miembros(req):
       return render(req,"miembros.html", {})

def consultas(req):
       return render(req,"consultas.html", {})

def sobre_mi(req):
       return render(req,"sobre_mi.html", {})

def form_miembro(req):
       
       
       if req.method == 'POST':

              MiFormulario_Miembro= formulario_miembro(req.POST)

              if MiFormulario_Miembro.is_valid():

                     data= MiFormulario_Miembro.cleaned_data

                     nuevo_miembro= Miembros(nombre= data['nombre'], apellido= data['apellido'], celular= data['celular'])
                     nuevo_miembro.save()

                     return render(req,"inicio.html", {"message": "¡BIENVENID@ SOS MIEMBRO DE LUDUS!"})
       
              else:
                     return render(req,"inicio.html", {"message": "UPS! Datos inválidos, vuelve a intentar."})

       else:
              MiFormulario_Miembro = formulario_miembro()
                     
       return render(req,"formulario_miembro.html", {"MiFormulario_Miembro": MiFormulario_Miembro})

def form_instructor(req):
       
       if req.method == 'POST':

              MiFormulario_Instructor= formularioinstructor(req.POST)

              if MiFormulario_Instructor.is_valid():

                     data= MiFormulario_Instructor.cleaned_data

                     nuevo_miembro= Instructores(nombre= data['nombre'], apellido= data['apellido'], celular= data['celular'])
                     nuevo_miembro.save()

                     return render(req,"inicio.html", {"message": "¡Nos pondremos en contacto sobre tu postulación!. El plazo es de 48hs hábiles."})
       
              else:
                     return render(req,"inicio.html", {"message": "UPS! Datos inválidos, vuelve a intentar."})

       else:
              MiFormulario_Instructor = formularioinstructor()
                     
       return render(req,"formularioinstructor.html", {"MiFormulario_Instructor": MiFormulario_Instructor})


def form_programa(req):
       
        if req.method == 'POST':

              MiFormulario_Programa= formularioprograma(req.POST)

              if MiFormulario_Programa.is_valid():

                     data= MiFormulario_Programa.cleaned_data

                     nuevo_programa= Programa(nombre= data['nombre'], duracion= data['duracion'], capacidad= data['capacidad'])
                     nuevo_programa.save()

                     return render(req,"inicio.html", {"message": "¡Nos pondremos en contacto sobre tu propuesta!. El plazo es de 48hs hábiles."})
       
              else:
                     return render(req,"inicio.html", {"message": "UPS! Datos inválidos, vuelve a intentar."})

        else:
              MiFormulario_Programa = formularioprograma()
                     
        return render(req,"formularioprograma.html", {"MiFormulario_Programa": MiFormulario_Programa})

def busqueda_programa(req):

       return render(req,"busqueda_programa.html", {})

def buscar(req):
       if req.GET["nombre"]:
              nombre = req.GET["nombre"]
              nombre = Programa.objects.filter(nombre__icontains= nombre)

              return render(req, "resultadobusquedaprograma.html", {"programa": nombre})
       
       else:
              return render(req, "inicio.html", {"message": "UPS! Hubo un error, volvé a intentar por favor."})

