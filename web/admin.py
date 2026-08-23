from django.contrib import admin
from .models import Solicitud

admin.site.site_header = "IEI Cuna Jardín Carlos Showing Ferrari"
admin.site.site_title = "Panel de Administración"
admin.site.index_title = "Bienvenido al Panel de Administración"


@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "asunto", "atendida", "fecha_creacion")
    list_filter = ("asunto", "atendida")
    search_fields = ("nombre", "apellido", "email")