# swagger_config.py

from drf_yasg import openapi

user_create_request_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre de usuario'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Contraseña'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Correo electrónico'),
    },
    required=['username', 'password', 'email'],
    example={
        'username': 'johndoe',
        'password': 'password123',
        'email': 'johndoe@example.com'
    }
)

user_create_response_example = openapi.Response(
    description="Usuario creado exitosamente",
    examples={
        'application/json': {
            'message': 'User registered successfully'
        }
    }
)

user_create_error_response_example = openapi.Response(
    description="Solicitud inválida",
    examples={
        'application/json': {
            'username': ['This field is required.'],
            'password': ['This field is required.'],
            'email': ['This field is required.']
        }
    }
)
