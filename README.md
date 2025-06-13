# 🛒 Web de Gestión de Productos - Trabajo Práctico

Este proyecto es una **aplicación web desarrollada con Django** que permite a los usuarios visualizar productos disponibles. Además, los usuarios registrados con permisos de **staff** pueden realizar operaciones **CRUD** (crear, leer, actualizar, eliminar) sobre productos, clientes y vendedores.

## 🚀 Funcionalidades principales

- Visualización pública de productos.
- Registro e inicio de sesión de usuarios.
- Sección "Acerca de mí" con información del desarrollador.
- Usuarios con permisos de **staff** pueden:
  - Crear, modificar y eliminar productos.
  - Administrar clientes y vendedores.
- Soporte para carga de imágenes (productos y avatar de usuario).
- Navegación adaptada según permisos de usuario.

## 🔩 Tecnologías utilizadas

- **Python 3**
- **Django 4**
- HTML + CSS (con Bootstrap para el diseño)
- Uso de modelos, vistas basadas en clases, formularios y herencia de templates.

## ⚙️ Instalación y ejecución

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/PedroMarchio/TuPrimeraPagina-Marchio.git
   cd TuPrimeraPagina-Marchio

2. Crear y activar un entorno virtual (En Windows):
    python -m venv venv
    venv\Scripts\activate 

3. Instalar las dependencias:
    pip install -r requirements.txt

4. Aplicar las migraciones:
    python manage.py migrate

5. Levantar el servidor:
    python manage.py runserver

6. Acceder desde el navegador a:
    http://127.0.0.1:8000/app/

Notas
La base de datos (db.blessing) y la carpeta media/ están ignoradas en el .gitignore.

Se utilizó herenciay navegación condicional según el tipo de usuario.

El proyecto incluye validaciones de seguridad para que solo el staff acceda a vistas sensibles, me paresio lo mejor para evitar que solo escribiendo el link el usuario pueda aceder de todas formas.

📫 Contacto
Desarrollado por Pedro Marchio