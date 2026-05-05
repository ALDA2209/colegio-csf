from django.shortcuts import render

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