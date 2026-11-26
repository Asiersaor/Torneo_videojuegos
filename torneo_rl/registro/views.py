from django.shortcuts import render, redirect
from .forms import FormularioRegistro, ModificacionCuenta
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from registro.models import Usuario
from inscripcion.models import Inscripcion

# Vistas de la aplicacion "registro", "inicio de sesion" y "panel de administrador".

def registro(request): # Vista para el formulario de registro.
    if request.method == "POST":
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("home")
    else:
        form = FormularioRegistro()
    return render(request, "registro/registro.html", {"form": form}) 

def inicio_sesion(request): # Vista para el formulario de inicio de sesion.
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect("home")
    else:
        form = AuthenticationForm(request)
    return render(request, "registro/inicio_sesion.html", {"form": form})

def cierre_sesion(request): # Vista para cerrar la sesion del usuario.
    if request.method == "POST":
        logout(request)
    return redirect("home")

@login_required
def cuenta_perfil(request): # Vista para mostrar los datos de la cuenta con la sesion iniciada.
    perfil_inscripcion = Inscripcion.objects.filter(usuario=request.user).first()
    return render(request, "registro/cuenta_perfil.html", {"perfil_inscripcion": perfil_inscripcion})

@login_required
def panel_admin(request): # Vista para mostrar el panel de administrador, solo accesible para el administrador.
    if request.user.rol != "admin":
        return redirect("home")
    usuarios = list(Usuario.objects.all())
    return render(request, "registro/panel_admin.html", {"usuarios": usuarios})

@login_required
def editar_usuario(request, id): # Vista para editar la informacion del usuario llamando al formulario para modificar el usuario.
    if request.user.rol != "admin":
        return redirect("home")
    usuario_existente = Usuario.objects.get(id=id)
    if request.method == "POST":
        form = ModificacionCuenta(request.POST,instance=usuario_existente)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
            return redirect("panel_admin")
    else:
        form = ModificacionCuenta(instance=usuario_existente)
    return render(request, "registro/modificacion_cuenta.html", {"form": form})

@login_required
def eliminar_usuario(request, id): # Vista para eliminar usuarios desde el panel de administrador.
    if request.user.rol != "admin":
        return redirect("home")
    usuario_existente = Usuario.objects.get(id=id)
    if request.method == "POST":
        usuario_existente.delete()
    return redirect("panel_admin")