# Ruta: mysite/cuentas/views.py
from django.shortcuts import render,redirect

"""
FORMULARIO PARA CREAR USUARIOS
FUCIONES PARA COMPROBRAR CREDENCIALES
"""

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password) #verficar credenciales
            if user is not None:
                login(request, user)
                return redirect('home') #redireccionar a la pagina principal
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form}) #renderizar el formulario  