from django.shortcuts import render, redirect
from django.core.mail import send_mail

def inicio(request):
    return render(request, 'web/index.html')

def nosotros(request):
    return render(request, 'web/nosotros.html')

def programas(request):
    return render(request, 'web/programas.html')

def cuna(request):
    return render(request, 'web/cuna.html')

def jardin3(request):
    return render(request, 'web/jardin3.html')

def jardin4(request):
    return render(request, 'web/jardin4.html')

def jardin5(request):
    return render(request, 'web/jardin5.html')

def galeria(request):
    return render(request, 'web/galeria.html')

def docentes(request):
    return render(request, 'web/docentes.html')

def contacto(request):
    enviado = False
    if request.method == "POST":
        nombre = request.POST.get("nombre", "")
        apellido = request.POST.get("apellido", "")
        email = request.POST.get("email", "")
        telefono = request.POST.get("telefono", "")
        nombre_nino = request.POST.get("nombre_nino", "")
        edad = request.POST.get("edad", "")
        asunto = request.POST.get("asunto", "")
        mensaje = request.POST.get("mensaje", "")
        cuerpo = "Nombre: " + nombre + " " + apellido + "\nCorreo: " + email + "\nTelefono: " + telefono + "\nNino: " + nombre_nino + "\nEdad: " + edad + "\nAsunto: " + asunto + "\n\nMensaje:\n" + mensaje
        send_mail(
            subject="Nuevo mensaje - " + nombre + " " + apellido,
            message=cuerpo,
            from_email="pasivi22@gmail.com",
            recipient_list=["pasivi22@gmail.com"],
        )
        enviado = True
    return render(request, "web/contacto.html", {"enviado": enviado})