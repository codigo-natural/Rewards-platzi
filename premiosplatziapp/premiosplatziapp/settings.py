"""
Django settings for premiosplatziapp project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
# Importamos la clase Path de la librería pathlib
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Definimos la variable BASE_DIR como la ruta absoluta al directorio padre del archivo "settings.py"
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(i&)h!#r%ac2*w7!3l-1!ko%37r#q82l4s*^g95)l*a$22)716'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Lista de hosts permitidos. Vacío significa que cualquier host está permitido.
ALLOWED_HOSTS = []


# Application definition
# Definición de aplicaciones instaladas en la aplicación
INSTALLED_APPS = [
    'django.contrib.admin', # proporciona la interfaz de administración de Django.
    'django.contrib.auth', # proporciona el sistema de autenticación de usuarios de Django.
    'django.contrib.contenttypes', # proporciona una forma de asociar contenido (modelos) con permisos.
    'django.contrib.sessions', # proporciona soporte para el manejo de sesiones de usuario.
    'django.contrib.messages', # proporciona soporte para mensajes de error en la aplicación.
    'django.contrib.staticfiles', #  proporciona soporte para la gestión de archivos estáticos (CSS, JavaScript, imágenes) en la aplicación.
]
THIRD_APPS = [
    #'jazzmin',
]

LOCAL_APPS = [
    'polls.apps.PollsConfig'
]

INSTALLED_APPS = THIRD_APPS + INSTALLED_APPS + LOCAL_APPS

# Definición de middleware utilizado en la aplicación
MIDDLEWARE = [
    # proporciona seguridad en la aplicación mediante la configuración de encabezados HTTP.
    'django.middleware.security.SecurityMiddleware',
    # proporciona soporte para el manejo de sesiones de usuario.
    'django.contrib.sessions.middleware.SessionMiddleware',
    #  proporciona funcionalidad común de middleware, como la configuración de encabezados HTTP y la redirección de URL.
    'django.middleware.common.CommonMiddleware',
    # proporciona protección contra ataques CSRF (Cross-Site Request Forgery).
    'django.middleware.csrf.CsrfViewMiddleware',
    # proporciona soporte para la autenticación de usuarios en la aplicación.
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # proporciona soporte para mensajes de error en la aplicación.
    'django.contrib.messages.middleware.MessageMiddleware',
    # proporciona protección contra ataques de clickjacking.
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# Configuración de la URL raíz de la aplicación
ROOT_URLCONF = 'premiosplatziapp.urls'

# Definición de plantillas para la aplicación
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# Configuración de la aplicación WSGI (interfaz de pasarela de servidor web)
WSGI_APPLICATION = 'premiosplatziapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

# Configuración de validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configuración de internacionalización
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
# Código de idioma predeterminado
LANGUAGE_CODE = 'en-us'
# Zona horaria predeterminada
TIME_ZONE = 'America/Bogota'
# Habilitar internacionalización
USE_I18N = True
# Habilitar zonas horarias
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# URL base para los archivos estáticos
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
# Tipo de campo de clave primaria predeterminado
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
