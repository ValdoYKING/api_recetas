# Recetas API

Una API para gestionar recetas de cocina, incluyendo autenticación de usuarios, roles y permisos. Esta API está construida con FastAPI y SQLAlchemy.

## Características

- Autenticación basada en JWT (JSON Web Tokens)
- Gestión de usuarios con roles y permisos
- CRUD (Crear, Leer, Actualizar, Eliminar) para recetas
- Endpoints protegidos para operaciones sensibles
- Documentación automática con Swagger UI

## Requisitos

- Python 3.7+
- Pip
- SQLite (por defecto, puedes cambiar a otra base de datos si lo prefieres)

## Instalación

1. Clona el repositorio:

   ```sh
   git clone https://github.com/tu_usuario/recetas-api.git
   cd recetas-api

2. Crea un entorno virtual e instala las dependencias:

   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   pip install -r requirements.txt

3. Configura las variables de entorno:
Crea un archivo .env en la raíz del proyecto y añade las siguientes variables:

   ```sh
   .env
   SECRET_KEY=tu_clave_secreta
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   DATABASE_URL=sqlite:///./test.db  # O la URL de tu base de datos preferida

4. Inicializa la base de datos:

    ```sh
    alembic upgrade head

5. Ejecuta la aplicación:

    ```sh
    uvicorn app.main:app --reload

## Uso
Una vez que la aplicación esté en funcionamiento, puedes acceder a la documentación automática generada por Swagger UI en http://127.0.0.1:8000/docs.

Endpoints Principales
/token: Obtiene un token de acceso.

/users/me: Obtiene la información del usuario actual.

/recipes/: CRUD para recetas.

Contribuir
Haz un fork del proyecto.

Crea una nueva rama para tu característica (git checkout -b nueva-caracteristica).

Realiza tus cambios y haz commit (git commit -am 'Añadir nueva característica').

Empuja tu rama (git push origin nueva-caracteristica).

Crea un nuevo Pull Request.

Licencia
Este proyecto está licenciado bajo los términos de la Licencia MIT.


### Resumen

1. **Descripción del Proyecto**: Proporciona una visión general de lo que hace la API.
2. **Características**: Enumera las características clave de la API.
3. **Requisitos**: Enumera los requisitos del entorno.
4. **Instalación**: Proporciona pasos detallados para clonar el repositorio, configurar el entorno y ejecutar la aplicación.
5. **Uso**: Explica cómo usar la API y acceder a la documentación.
6. **Contribuir**: Describe cómo contribuir al proyecto.
7. **Licencia**: Incluye la información de la licencia.

Puedes ajustar y personalizar este archivo según las necesidades específicas de tu proyecto. Si tienes alguna pregunta o necesitas más detalles, ¡házmelo saber! 😊🚀 Continuemos con el desarrollo. 💡🔧