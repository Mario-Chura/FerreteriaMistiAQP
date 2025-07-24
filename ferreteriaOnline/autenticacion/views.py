from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.conf import settings

from .forms import RegistroForm

class VRegistro(View):

    def get(self, request):
        form = RegistroForm()
        return render(request, "registro/registro.html", {"form": form})

    def post(self, request):
        form = RegistroForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            
            # Enviar email de bienvenida
            self.enviar_email_bienvenida(usuario)
            
            # Loguear automáticamente al usuario
            login(request, usuario)
            
            messages.success(request, f'¡Bienvenido {usuario.first_name}! Tu cuenta ha sido creada exitosamente.')
            return redirect('Index')

        else:
            # Mostrar errores específicos
            for field, errors in form.errors.items():
                for error in errors:
                    if hasattr(form.fields[field], 'label') and form.fields[field].label:
                        messages.error(request, f'{form.fields[field].label}: {error}')
                    else:
                        messages.error(request, f'{error}')

            return render(request, "registro/registro.html", {"form": form})

    def enviar_email_bienvenida(self, usuario):
        """Envía email de bienvenida al nuevo usuario"""
        try:
            asunto = "¡Bienvenido a Ferretería Misti!"
            mensaje = f"""
Hola {usuario.first_name},

¡Bienvenido a Ferretería Misti!

Tu cuenta ha sido creada exitosamente con los siguientes datos:
- Usuario: {usuario.username}
- Email: {usuario.email}
- Nombre: {usuario.first_name} {usuario.last_name}

Ya puedes comenzar a explorar nuestros productos y realizar tus compras.

¡Gracias por elegirnos!

Equipo de Ferretería Misti
            """
            
            send_mail(
                asunto,
                mensaje,
                settings.EMAIL_HOST_USER,
                [usuario.email],
                fail_silently=False,
            )
        except Exception as e:
            # Log del error pero no afecta el registro
            print(f"Error enviando email de bienvenida: {e}")

def cerrar_sesion(request):
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('Index')

def logear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                # Mostrar nombre si existe, sino username
                nombre_mostrar = usuario.first_name if usuario.first_name else usuario.username
                messages.success(request, f'¡Hola {nombre_mostrar}! Has iniciado sesión correctamente.')
                return redirect('Index')
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
        else:
            messages.error(request, "Por favor, corrige los errores en el formulario")

    form = AuthenticationForm()
    return render(request, "login/login.html", {"form": form})