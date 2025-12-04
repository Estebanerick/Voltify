from django.urls import path
from . import views

urlpatterns = [
    # Páginas principales
    path('', views.index, name='index'),
    path('inicio/', views.inicio, name='inicio'),
    
    # Páginas de cálculo
    path('consumo-mensual/', views.consumo_mensual, name='consumo_mensual'),
    path('consumo-individual/', views.consumo_individual, name='consumo_individual'),
    path('historial/', views.historial, name='historial'),
    path('seleccionar-artefacto-hogar/', views.seleccionar_artefacto_hogar, name='seleccionar_artefacto_hogar'),
    path('seleccionar-artefacto-individual/', views.seleccionar_artefacto_individual, name='seleccionar_artefacto_individual'),
    
    # Página de datos curiosos
    path('sabias-que/', views.sabias_que, name='sabias_que'),
    
    # Páginas legales
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    
    # Autenticación
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]