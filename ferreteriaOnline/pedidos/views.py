from django.contrib import messages
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from carro.carro import Carro

from pedidos.models import LineaPedido, Pedido

from django.template.loader import render_to_string

from django.utils.html import strip_tags

from django.core.mail import send_mail

from tienda.models import Producto


# Create your views here.


@login_required(login_url='/autenticacion/logear')
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user) # damos de alta un pedido
    carro = Carro(request)  # cogemos el carro
    lineas_pedido = list()  # lista con los pedidos para recorrer los elementos del carro
    for key, value in carro.carro.items(): #recorremos el carro con sus items
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido                 
            ))

    LineaPedido.objects.bulk_create(lineas_pedido) # crea registros en BBDD en paquete
    
    # Limpiar el carro después del pedido
    carro.limpiar_carro()
    
    # Debug: Verificar el email del usuario
    print(f"Email del usuario: {request.user.email}")
    print(f"Username: {request.user.username}")
    
    #enviamos mail al cliente
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        email_usuario=request.user.email
    )
    
    #mensaje para el futuro
    messages.success(request, "El pedido se ha creado correctamente")
    
    return redirect('../tienda')
    

def enviar_mail(**kwargs):
    # Debug: Verificar que lleguen los datos
    print(f"Datos recibidos en enviar_mail:")
    print(f"  - Pedido: {kwargs.get('pedido')}")
    print(f"  - Email usuario: {kwargs.get('email_usuario')}")
    print(f"  - Nombre usuario: {kwargs.get('nombreusuario')}")
    
    asunto = "Gracias por tu pedido - Ferretería Misti"
    mensaje = render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario": kwargs.get("nombreusuario"),
        "email_usuario": kwargs.get("email_usuario")
    })

    mensaje_texto = strip_tags(mensaje)
    from_email = "ferreteriaaqpmisti@gmail.com"
    to = kwargs.get("email_usuario")  # Email del cliente
    
    # Enviar email al cliente y copia a la ferretería
    send_mail(
        asunto, 
        mensaje_texto, 
        from_email, 
        [to, "ferreteriaaqpmisti@gmail.com"], 
        html_message=mensaje
    )