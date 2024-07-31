# myapp/tests/test_endpoints.py

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

@pytest.mark.django_db
def test_property_endpoints(client):
    # Crear un usuario
    User = get_user_model()
    user = User.objects.create_user(username="testuser", password="testpass")

    # Autenticación del usuario (si es necesario)
    client.login(username="testuser", password="testpass")
    
    # Realizar una solicitud a un endpoint
    url = reverse('api/auth/register/')  # Cambia esto a la URL que deseas probar
    response = client.get(url)

    # Asegúrate de que la respuesta sea la esperada
    assert response.status_code == 200
    assert 'some expected content' in response.content.decode()
