from django.shortcuts import render, redirect
from .models import Usuario
from .forms import Name


# Create your views here.



def VentanaPrincipal (request):
    return render (request, 'VentanaPrincipal.html')


def Noticias(request):
    return render (request, 'Noticias.html')

def Sesion(request):
    return render (request, 'Sesion.html')

def VarianteDelta (request):
    return render (request, 'variantedelta.html')

def Charquican (request):
    return render (request, 'Charquican.html')

def bravovidal (request):
    return render (request, 'BravoVidal.html')


def ingresar (request):
    if request.method=="post":
        registro=Name(request.POST, files=request.FILES)
        if registro.is_valid():
            registro.save()
            return redirect ('ver')
        else:
            registro=Name()
    return render(request, 'core/AnadirUsuario.html',{'registro':Name})

def modificarusuario (request,id):
    user=Usuario.objects.get(Rut=id)
    datos={
        'form':Name(instance=user)
    }
    if request.method=="post":
        Modificar=Name(request.POST, files=request.FILES,instance=user)
        if Modificar.is_valid():
            Modificar.save()
            return redirect('ver')
    return render(request,'core/ModificarUsuario.html',datos)


    

def eliminar (request,id):
    eliminarusuario=Usuario.objects.get(Rut=id)
    eliminarusuario.delete()
    return redirect('ver')


def ver (request):
    datos=Usuario.objects.all()
    return render (request,'core/ver.html',context={'Datos':datos} )



   
