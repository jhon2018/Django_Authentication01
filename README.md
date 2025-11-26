# --SESSION 4
## USUARIO  GIT
git config user.name
git config user.email

## INSTALAR
python -m venv .venv
python --version
pip install django

## VER TUS INSTALACIONES DENTRO DE (.venv)
pip list
python -m pip freeze > requirements.txt

## CREAR PROYECTO - CARPETA PRINCIPAL  mysite
django-admin startproject mysite  (dentro de esta carpeta iran todos los archivos y carpetas de tu proyecto)

## EJECUTAR EN EL SERVIDOR (verificar dentro de mysite)
python manage.py runserver
python manage.py runserver 7000 (opcional)

## CREAR APP - DENTRO LA CARPETA PRINCIPAL accounts y OJO agregar al INSTALLED_APPS
ir a mysite\settings.py ir INSTALLED_APPS
python manage.py startapp accounts

## CREAR NUEVAS DEPENDENCIAS
buscalo asi: 1 dependencias

## MIGRAR TABLAS POR QUE VERAS EN CONSOLA EL  : You have 18 unapplied migration(s).
mysite> python manage.py migrate

## USAMOS FRAMEWOKD DE ECENARIO DE LOGIN
UserCreationForm,login,authenticate DE  django.contrib.auth 

# ARCHIVOS 
base.html -> home.html -> signup.html -> login.html


# levanta la web administrador
http://127.0.0.1:8000/admin


## CREAR EL SUPERUSUARIO (MAYOR NIVEL)
python manage.py createsuperuser  

user:jveras
password: 47736559

user:jmallqui (inicar session formulario)
password: 47736_#21

# EXPLICACION
## mysite/mysite/ → CONFIGURACIÓN DEL PROYECTO

ARCHIVOS PRINCIPALES:

settings.py → Configuración global (BD, apps, seguridad, etc.)

urls.py → Rutas principales del proyecto

wsgi.py → Configuración para producción (servidores web)

asgi.py → Configuración para aplicaciones asíncronas