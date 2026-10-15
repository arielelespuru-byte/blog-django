# 📝 Blog Web en Django

## Descripción del Proyecto
Aplicación web de blog desarrollada en Django que permite la gestión completa de publicaciones (CRUD), carga de imágenes, registro de usuarios y autenticación con rutas protegidas.

---

## Criterios de Aceptación Cumplidos
- **Gestión de Posts (CRUD):** Crear, leer, editar y eliminar publicaciones.
- **Soporte Multimedia:** Carga y despliegue de imágenes para cada post (librería `Pillow`).
- **Autenticación:** Registro de usuarios, inicio y cierre de sesión.
- **Seguridad:** Vistas protegidas con `@login_required` para evitar que usuarios no autenticados creen, editen o eliminen posts.
- **Diseño Responsive:** Interfaz limpia construida con Bootstrap 5.

---

## Tecnologías Utilizadas
* Python 3.x
* Django
* SQLite
* Pillow (para procesamiento de imágenes)
* Bootstrap 5

---

## Instrucciones de Instalación Local

1. **Clonar el repositorio y entrar a la carpeta del proyecto:**
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd blog-django