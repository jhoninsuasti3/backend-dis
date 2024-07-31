# backend-dis
Backend Python + Django + DRF + Pytest + JWT + Docker + Github Actions + PostgreSQL + Swagger + AWS - aplicación web de gestión de propiedades inmobiliarias. La aplicación permitirá  a los usuarios (agentes inmobiliarios) crear, leer, actualizar y eliminar registros de propiedades.


## Clonar el Repositorio

1. Abre una terminal o línea de comandos.
2. Clona el repositorio usando Git:

    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    ```

3. Navega al directorio del proyecto:

    ```bash
    cd tu-repositorio
    ```

## Configurar el Entorno Virtual

1. Crea un entorno virtual en el directorio del proyecto:

    ```bash
    python -m venv venv
    ```

2. Activa el entorno virtual:

    - **En Windows:**

        ```bash
        venv\Scripts\activate
        ```

    - **En macOS y Linux:**

        ```bash
        source venv/bin/activate
        ```

## Instalar las Dependencias

1. Asegúrate de que el entorno virtual esté activado.
2. Instala las dependencias del proyecto:

    ```bash
    pip install -r requirements.txt
    ```

## Ejecutar las Migraciones

1. Aplica las migraciones para configurar la base de datos:

    ```bash
    python manage.py migrate
    ```

2. (Opcional) Crea un superusuario para acceder al panel de administración de Django:

    ```bash
    python manage.py createsuperuser
    ```

    Sigue las instrucciones para proporcionar un nombre de usuario, correo electrónico y contraseña para el superusuario.

## Correr el Servidor

1. Ejecuta el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

2. Accede a la aplicación en tu navegador web en la siguiente URL:

    ```
    http://127.0.0.1:8000/
    ```

3. (Opcional) Para acceder al panel de administración de Django, ve a:

    ```
    http://127.0.0.1:8000/admin/
    ```

    Inicia sesión con las credenciales del superusuario que creaste anteriormente.

## Información Adicional

- **Dependencias del Proyecto:** Las dependencias están listadas en el archivo `requirements.txt`.
- **Configuración de Base de Datos:** La configuración de la base de datos se encuentra en el archivo `settings.py`.

## Contribuciones

Si deseas contribuir al proyecto, por favor sigue los siguientes pasos:

1. Realiza un fork del repositorio.
2. Crea una rama para tu característica o corrección de errores.
3. Realiza los cambios y prueba que todo funcione correctamente.
4. Envía un pull request describiendo los cambios realizados.

## Contacto

Para cualquier pregunta o problema, por favor contacta al desarrollador principal a través del correo electrónico: tu-email@example.com

---

¡Gracias por contribuir y usar el proyecto!

