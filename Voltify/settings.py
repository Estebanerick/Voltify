"""
Django settings for Voltify project.
"""

import os
import socket
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 
    'django-insecure-voltify-pro-2024-chile-energy-control-secret-key'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# ============================================================================
# ALLOWED_HOSTS - Configuración optimizada para Render
# ============================================================================

# Obtener hostname de Render automáticamente
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS = [RENDER_EXTERNAL_HOSTNAME]
else:
    ALLOWED_HOSTS = []

# Hosts base
ALLOWED_HOSTS.extend([
    'voltify.onrender.com',
    '127.0.0.1', 
    'localhost', 
    '0.0.0.0',
])

# Para desarrollo local
if DEBUG:
    try:
        # Obtener IP local
        local_ip = socket.gethostbyname(socket.gethostname())
        ALLOWED_HOSTS.append(local_ip)
        ALLOWED_HOSTS.append('*')  # Solo en desarrollo
    except:
        pass

# Agregar dominio de Render genérico (debe estar al final)
ALLOWED_HOSTS.append('.onrender.com')

# ============================================================================
# Application definition
# ============================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mi_app',
    'whitenoise.runserver_nostatic',  # Para desarrollo con WhiteNoise
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Debe estar después de SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Voltify.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Si tienes templates globales
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'Voltify.wsgi.application'

# ============================================================================
# Database - PostgreSQL en Render, SQLite localmente
# ============================================================================

# Configuración de base de datos para Render
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    # Producción en Render (PostgreSQL)
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            conn_health_checks=True,
            ssl_require=True
        )
    }
    
    # Optimización para PostgreSQL
    DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql'
    
else:
    # Desarrollo local (SQLite)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
            'OPTIONS': {
                'timeout': 20,
            }
        }
    }

# ============================================================================
# Password validation
# ============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ============================================================================
# Internationalization
# ============================================================================

LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ============================================================================
# Static files (CSS, JavaScript, Images) - Configuración para Render
# ============================================================================

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # IMPORTANTE para collectstatic

# Directorios adicionales de archivos estáticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'mi_app/static'),
    os.path.join(BASE_DIR, 'static'),  # Si tienes static global
]

# Configuración de WhiteNoise para archivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configuración de WhiteNoise (opcional, para mejor rendimiento)
WHITENOISE_USE_FINDERS = True
WHITENOISE_MANIFEST_STRICT = False
WHITENOISE_ALLOW_ALL_ORIGINS = True

# ============================================================================
# Media files (uploads de imágenes, documentos, etc.)
# ============================================================================

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Crear directorios si no existen
os.makedirs(MEDIA_ROOT, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)

# ============================================================================
# Default primary key field type
# ============================================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ============================================================================
# Authentication URLs
# ============================================================================

LOGIN_REDIRECT_URL = 'inicio'
LOGOUT_REDIRECT_URL = 'index'
LOGIN_URL = 'login'

# ============================================================================
# Security settings - Configuración diferente para desarrollo/producción
# ============================================================================

if not DEBUG:
    # ===================== PRODUCCIÓN (Render) =====================
    
    # SSL/HTTPS
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    
    # Cookies seguras
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = True
    SESSION_COOKIE_HTTPONLY = True
    
    # HSTS (HTTP Strict Transport Security)
    SECURE_HSTS_SECONDS = 31536000  # 1 año
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    
    # Otras cabeceras de seguridad
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    
    # CSRF Trusted Origins para Render
    CSRF_TRUSTED_ORIGINS = [
        'https://voltify.onrender.com',
        'https://*.onrender.com',
        'https://*.render.com',
    ]
    
    # Añadir automáticamente el hostname de Render a CSRF
    if RENDER_EXTERNAL_HOSTNAME:
        CSRF_TRUSTED_ORIGINS.append(f'https://{RENDER_EXTERNAL_HOSTNAME}')
    
else:
    # ===================== DESARROLLO LOCAL =====================
    
    # Desactivar SSL para desarrollo
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    
    # Orígenes CSRF para desarrollo
    CSRF_TRUSTED_ORIGINS = [
        'http://localhost:8000',
        'http://127.0.0.1:8000',
        'http://0.0.0.0:8000',
    ]

# ============================================================================
# Messages framework (Tailwind CSS classes)
# ============================================================================

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'bg-gray-100 border-gray-400 text-gray-700',
    messages.INFO: 'bg-blue-100 border-blue-400 text-blue-700',
    messages.SUCCESS: 'bg-green-100 border-green-400 text-green-700',
    messages.WARNING: 'bg-yellow-100 border-yellow-400 text-yellow-700',
    messages.ERROR: 'bg-red-100 border-red-400 text-red-700',
}

# ============================================================================
# Logging configuration para Render
# ============================================================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': 'INFO',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
            'formatter': 'verbose',
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': True,
        },
        'mi_app': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': False,
        },
    },
}

# ============================================================================
# Performance optimizations
# ============================================================================

# Cache (simple para desarrollo, usar Redis/Memcached en producción)
if not DEBUG and DATABASE_URL:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'django_cache_table',
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'unique-snowflake',
        }
    }

# Compresión de respuestas
if not DEBUG:
    MIDDLEWARE.insert(1, 'django.middleware.gzip.GZipMiddleware')

# ============================================================================
# Render-specific optimizations
# ============================================================================

# Tiempo de vida de conexiones a la base de datos
if DATABASE_URL:
    DATABASES['default']['CONN_MAX_AGE'] = 600  # 10 minutos

# Configuración para el correo (si necesitas)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' if DEBUG else 'django.core.mail.backends.smtp.EmailBackend'

# ============================================================================
# App-specific settings
# ============================================================================

# Aquí puedes agregar configuraciones específicas de tu aplicación
# por ejemplo:
# VOLTIFY_MAX_VEHICLES = int(os.environ.get('VOLTIFY_MAX_VEHICLES', 10))
# VOLTIFY_API_KEY = os.environ.get('VOLTIFY_API_KEY', '')

# ============================================================================
# Final initialization
# ============================================================================

print(f"=== Configuración cargada ===")
print(f"DEBUG: {DEBUG}")
print(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")
print(f"Database: {'PostgreSQL' if DATABASE_URL else 'SQLite'}")
print(f"Static root: {STATIC_ROOT}")
print(f"==============================")