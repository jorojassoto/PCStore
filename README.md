# PCStore - E-commerce de Componentes de PC (Django + SQL Server)

Este proyecto es un sistema e-commerce básico para venta de componentes de PC, desarrollado con Django y conectado a una base de datos SQL Server.

## 📦 Características

- Registro y listado de componentes, categorías y marcas.
- Relación de modelos funcional.
- Autenticación de usuarios.
- Carrito de compras básico con total.
- Conexión a SQL Server mediante `django-mssql-backend`.

## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/jorojassoto/PCStore.git
cd PCStore
```
2. Crea un entorno virtual e instala dependencias:
```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```
3. Configura tu conexión en PCStore/settings.py
```bash
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'TuBaseDeDatos',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'extra_params': 'TrustServerCertificate=yes;',
        },
    }
}
```
4. Ejecuta migraciones y crea un superusuario:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
5. Ejecuta el servidor:
```bash
python manage.py runserver
```


