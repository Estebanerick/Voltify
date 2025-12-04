from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    """Página principal del sitio Voltify Pro"""
    return render(request, 'mi_app/index.html')

@login_required
def inicio(request):
    """Dashboard principal después del login"""
    context = {
        'user': request.user
    }
    return render(request, 'mi_app/inicio.html', context)

@login_required
def consumo_mensual(request):
    """Vista para el cálculo de consumo mensual"""
    context = {
        'user': request.user
    }
    return render(request, 'mi_app/consumo_mensual.html', context)

@login_required
def consumo_individual(request):
    """Vista para el cálculo de consumo individual"""
    context = {
        'user': request.user
    }
    return render(request, 'mi_app/consumo_individual.html', context)

@login_required
def historial(request):
    """Vista para el historial de consumos"""
    context = {
        'user': request.user
    }
    return render(request, 'mi_app/historial.html', context)

@login_required
def seleccionar_artefacto_hogar(request):
    """Vista para seleccionar artefactos del hogar"""
    context = {
        'user': request.user
    }
    return render(request, 'mi_app/seleccionar_artefacto_hogar.html', context)

@login_required
def seleccionar_artefacto_individual(request):
    """Vista para seleccionar artefactos individuales"""
    context = {
        'user': request.user
    }
    return render(request, 'mi_app/seleccionar_artefacto_individual.html', context)

def sabias_que(request):
    """Página con datos curiosos sobre energía eléctrica"""
    return render(request, 'mi_app/sabias_que.html')

def terms(request):
    """Página de términos de servicio"""
    return render(request, 'mi_app/terms.html')

def privacy(request):
    """Página de política de privacidad"""
    return render(request, 'mi_app/privacy.html')

def login_view(request):
    """Vista personalizada para login"""
    if request.user.is_authenticated:
        messages.info(request, 'Ya tienes una sesión activa.')
        return redirect('inicio')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido de nuevo {username}!')
                return redirect('inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos. Por favor intenta nuevamente.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

def register_view(request):
    """Vista personalizada para registro"""
    if request.user.is_authenticated:
        messages.info(request, 'Ya tienes una sesión activa.')
        return redirect('inicio')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'¡Cuenta creada exitosamente! Bienvenido {user.username}.')
            return redirect('inicio')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    """Vista para cerrar sesión"""
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente. ¡Te esperamos pronto!')
    return redirect('index')