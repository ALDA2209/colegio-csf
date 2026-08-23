from django.db import models


class Solicitud(models.Model):
    ASUNTO_CHOICES = [
        ("programas", "Consulta sobre programas educativos"),
        ("visita", "Solicitar visita al colegio"),
        ("otro", "Otro"),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    nombre_nino = models.CharField(max_length=100, blank=True)
    edad = models.CharField(max_length=10, blank=True)
    asunto = models.CharField(max_length=20, choices=ASUNTO_CHOICES)
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    atendida = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solicitudes"
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.get_asunto_display()}"