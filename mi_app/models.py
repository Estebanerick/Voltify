from django.db import models
from django.contrib.auth.models import User

# Los modelos para la aplicación de control de energía se agregarán después
# Por ahora solo usamos el modelo User por defecto de Django

class PerfilUsuario(models.Model):
    """Perfil extendido para usuarios de Voltify Pro"""
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"
    
    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuarios"