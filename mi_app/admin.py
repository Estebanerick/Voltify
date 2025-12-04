from django.contrib import admin
from .models import PerfilUsuario

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefono', 'ciudad', 'fecha_creacion')
    list_filter = ('ciudad', 'fecha_creacion')
    search_fields = ('usuario__username', 'telefono', 'ciudad')
    date_hierarchy = 'fecha_creacion'