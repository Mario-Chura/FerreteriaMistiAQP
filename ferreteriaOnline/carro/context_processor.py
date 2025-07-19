def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        # Verificar si existe la sesión del carro antes de acceder
        carro = request.session.get("carro", {})
        if carro:
            for key, value in carro.items():
                total = total + float(value["precio"])  
        else:
            total = 0
    else:
        total = "Debes Iniciar sesión"    

    return {"importe_total_carro": total}