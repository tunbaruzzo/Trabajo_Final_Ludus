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
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

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

def paginaerror(req):
       return render(req, "paginaerror.html", {})

def form_miembro(req):
       
       
       if req.method == 'POST':

              MiFormulario_Miembro= formulario_miembro(req.POST)

              if MiFormulario_Miembro.is_valid():

                     data= MiFormulario_Miembro.cleaned_data

                     nuevo_miembro= Miembros(nombre= data['nombre'], apellido= data['apellido'], celular= data['celular'])
                     nuevo_miembro.save()

                     return render(req,"miembros.html", {"message": "¡BIENVENID@ SOS MIEMBRO DE LUDUS!"})
       
              else:
                     return render(req,"miembros.html", {"message": "UPS! Datos inválidos, vuelve a intentar."})

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

                     return render(req,"instructores.html", {"message": "¡Nos pondremos en contacto sobre tu postulación! El plazo es de 48hs hábiles."})
       
              else:
                     return render(req,"instructores.html", {"message": "UPS! Algo pasó, comunicate con nosotros."})

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

                     return render(req,"programa.html", {"message": "¡Nos pondremos en contacto sobre tu propuesta! El plazo es de 48hs hábiles."})
       
              else:
                     return render(req,"programa.html", {"message": "UPS! Datos inválidos, vuelve a intentar."})

        else:
              MiFormulario_Programa = formularioprograma()
                     
        return render(req,"formularioprograma.html", {"MiFormulario_Programa": MiFormulario_Programa})


def leer_miembros(req):
       listamiembros = Miembros.objects.all()

       return render (req, "leer_miembros.html", {"miembros": listamiembros})

def eliminar_miembros(req, id):
       if req.method == 'POST':

              miembro = Miembros.objects.get(id=id)
              miembro.delete()

              listamiembros = Miembros.objects.all()

       return render (req, "leer_miembros.html", {"miembros": listamiembros})

def editar_miembros(req, id):
       if req.method == 'POST':

              MiFormulario_Miembro= formulario_miembro(req.POST)

              if MiFormulario_Miembro.is_valid():

                     data= MiFormulario_Miembro.cleaned_data

                     miembro = Miembros.objects.get(id=id)

                     miembro.nombre= data["nombre"]
                     miembro.apellido= data["apellido"]
                     miembro.celular=data["celular"]

                     miembro.save()

                     return render(req,"miembros.html", {"message": "Datos actualizados exitosamente."})
       
              else:
                     return render(req,"editar_miembros.html", {"message": "UPS! Datos inválidos, vuelve a intentar."})

       else:
              miembro = Miembros.objects.get(id=id)

              MiFormulario_Miembro = formulario_miembro(initial={
                     "nombre": miembro.nombre,
                     "apellido": miembro.apellido,
                     "celular": miembro.celular
              })
                     
       return render(req,"editar_miembros.html", {"MiFormulario_Miembro": MiFormulario_Miembro, "id":miembro.id})


class listadeprogramas(ListView):
       model = Programa
       template_name= 'listadeprogramas.html'
       context_object_name= "Programas"

class programadetail(DetailView):
       model= Programa
       template_name= 'programadetail.html'
       context_object_name= "Programa"

class programacreacion(CreateView):
       model= Programa
       template_name= 'programacreacion.html'
       fields= ["nombre"]
       success_url= "/Principal/"

class programaeditar(UpdateView):
       model= Programa
       template_name= 'programaeditar.html'
       fields=('__all__')
       success_url= "/Principal/"
       context_object_name= "programa"

class programaeliminar(DeleteView):
       model= Programa
       template_name='programaeliminar.html'
       success_url= "/Principal/"
