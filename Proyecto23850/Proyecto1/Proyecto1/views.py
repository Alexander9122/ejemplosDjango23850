from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime
from django.template import loader

def saludo(request):
    return HttpResponse("Soy Jorge - Hola Django - Coder")

def segundaVista(request):

    return HttpResponse ("<br><br>---------------YA SOMOS PROGRAMADORES WEB-----------------")

def dia(request):

    variable = datetime.now()

    return HttpResponse(f"Hoy es un gran dia <br> {variable}")

def apellido(request, ape):

    fecha = datetime.now()
    return HttpResponse(f"El profe de coder {ape}, es muy bueno..<br><br>..Por lo menos Hoy:{fecha}")

def CalculoEdad(request, anio):

    hoy  = datetime.now()
    year = int(hoy.year)
    anio = int(anio)
    edad = (year - anio)
    
    return HttpResponse(f"La edad del usuario es {edad} Años")


def probandoTemplate(request):

    mejorEstudiante = "Jorge Alexander"

    nota = 8.9

    fecha = datetime.now

    estudiantesSimpaticos = ["Jorge", "Danny","Paola"]

    dicc = {"nombre":mejorEstudiante, "nota":nota, "fecha": fecha, "estudiantes": estudiantesSimpaticos}

    plantilla = loader.get_template("template1.html")

#    miHTML = open("C:/Users/jlale/OneDrive/Documentos/ejemplosDjango23850/Proyecto23850/Proyecto1/Proyecto1/plantillas/template1.html")

#   plantilla = Template(miHTML.read())

#   miHTML.close()

#    miContexto = Context(dicc)

#    documento = plantilla.render(miContexto)

    documento = plantilla.render(dicc)

    return HttpResponse(documento)