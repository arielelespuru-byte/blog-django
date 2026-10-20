# 📝 Blog Web en Django

## Descripción del Proyecto
Aplicación web de blog desarrollada en **Django** como proyecto final. Permite la gestión completa de contenidos mediante un sistema **CRUD** (Crear, Leer, Actualizar, Eliminar), administración de perfiles de usuario, autenticación segura y carga de imágenes multimedia.

---

## 🚀 Características Principales
- **Gestión de Posts:** Creación, edición, visualización detallada y eliminación de publicaciones.
- **Sistema de Autenticación:** Registro de nuevos usuarios, inicio y cierre de sesión seguros.
- **Vistas de Perfil:** Panel personalizado donde cada usuario autenticado puede visualizar sus datos de cuenta y gestionar exclusivamente sus propias publicaciones.
- **Control de Accesos:** Rutas protegidas mediante decoradores (`@login_required`) para impedir acciones no autorizadas.
- **Soporte Multimedia:** Carga de imágenes dinámicas utilizando la librería `Pillow`.
- **Diseño Responsive:** Interfaz moderna y adaptable desarrollada con **Bootstrap 5**.

---

## 🛠️ Tecnologías y Librerías Utilizadas
* **Python** (Versión 3.x)
* **Django** (Framework Web)
* **SQLite** (Base de datos relacional)
* **Pillow** (Procesamiento de imágenes)
* **Bootstrap 5** (Diseño frontend)

---

## ⚙️ Instrucciones de Instalación y Ejecución Local

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd blog-django