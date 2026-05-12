from django.shortcuts import render, redirect
import requests
import os

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

        api_key = os.environ.get("BREVO_API_KEY", "")
        url = "https://api.brevo.com/v3/smtp/email"
        headers = {
            "accept": "application/json",
            "api-key": api_key,
            "content-type": "application/json"
        }
        data = {
            "sender": {"name": "Colegio CSF", "email": "ab1c46001@smtp-brevo.com"},
            "to": [{"email": "pasivi22@gmail.com"}],
            "subject": "Nuevo mensaje - " + nombre + " " + apellido,
            "textContent": cuerpo
        }
        requests.post(url, json=data, headers=headers)
        enviado = True
    return render(request, "web/contacto.html", {"enviado": enviado})
