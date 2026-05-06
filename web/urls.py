from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('programas/', views.programas, name='programas'),
    path('programas/cuna/', views.cuna, name='cuna'),
    path('programas/jardin3/', views.jardin3, name='jardin3'),
    path('programas/jardin4/', views.jardin4, name='jardin4'),
    path('programas/jardin5/', views.jardin5, name='jardin5'),
    path('galeria/', views.galeria, name='galeria'),
    path('docentes/', views.docentes, name='docentes'),
    path('contacto/', views.contacto, name='contacto'),
]
