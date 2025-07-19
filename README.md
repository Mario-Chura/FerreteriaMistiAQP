# Ferretería Misti AQP

## Correo y contraseña de la empresa
- **Correo**: ferreteriaaqpmisti@gmail.com
- **Contraseña**: MantenimientoAQP

## Levantar localmente

### Clonar el repositorio
```bash
git clone https://github.com/Mario-Chura/FerreteriaMistiAQP.git
```

### Crear entorno virtual
```bash
python -m venv venv_ferreteria
```

### Activar entorno virtual
```bash
venv_ferreteria\Scripts\activate
```

### Asegúrate de que el entorno virtual esté activado
```bash
(venv_ferreteria) ….erreteriaMistiAQP>
```

### Actualizar pip
```bash
python -m pip install --upgrade pip
```

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Acceder al directorio
```bash
cd .\ferreteriaOnline\
```

### Aplicar migraciones
```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

### Probar el servidor
```bash
python manage.py runserver
```

## Acceder
http://127.0.0.1:8000/

## Credenciales del admin
- **Usuario**: FerreteriaMistiAQP
- **Contraseña**: Misti_AQP