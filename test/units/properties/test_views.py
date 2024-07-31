# tests/integration/test_property_views.py

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from properties.models import Property


ENDPOINT = "/api/pre-loans"


@pytest.mark.django_db
def test_property_list_view(client):
    # Crear un usuario
    User = get_user_model()
    user = User.objects.create_user(username="testuser", password="testpass")
    
    # Autenticación del usuario
    client.login(username="testuser", password="testpass")

    # Crear algunas propiedades para la prueba
    Property.objects.create(
        address="En daguita",
        price=150000.00,
        size=1200,
        description="Esta es una.",
        property_type="house",
        bedrooms=3,
        bathrooms=2,
        parking_spaces=2,
        year_built=2000,
        is_furnished=True
    )
    
    Property.objects.create(
        address="En daguita",
        price=250000.00,
        size=2000,
        description="Mi casa vieja",
        property_type="house",
        bedrooms=4,
        bathrooms=3,
        parking_spaces=3,
        year_built=2010,
        is_furnished=False
    )

    # Realizar la solicitud GET
    url = reverse('/api/properties/')  # 
    response = client.get(url, {'property_type': 'house', 'min_price': 100000})
    
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 2  # Verifica que las dos propiedades se devuelvan

@pytest.mark.django_db
def test_property_create_view(client):
    # Crear un usuario
    User = get_user_model()
    user = User.objects.create_user(username="testuser", password="testpass")
    
    # Autenticación del usuario
    client.login(username="testuser", password="testpass")

    # Datos para crear una nueva propiedad
    data = {
        "address": "Direccion ejemplo",
        "price": 200000.00,
        "size": 1500,
        "description": "casita.",
        "property_type": "apartmento",
        "bedrooms": 2,
        "bathrooms": 1,
        "parking_spaces": 1,
        "year_built": 2015,
        "is_furnished": True
    }

    # Realizar la solicitud POST
    url = reverse('property-list')  # 
    response = client.post(url, data, format='json')
    
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['address'] == "Direccion ejemplo"


@pytest.mark.django_db
def test_property_update_view(client):
    # Crear un usuario
    User = get_user_model()
    user = User.objects.create_user(username="testuser", password="testpass")
    
    # Autenticación del usuario
    client.login(username="testuser", password="testpass")

    # Crear una propiedad
    property_instance = Property.objects.create(
        address="La elsa",
        price=150000.00,
        size=1200,
        description="Casa buena",
        property_type="house",
        bedrooms=3,
        bathrooms=2,
        parking_spaces=2,
        year_built=2000,
        is_furnished=True
    )

    # Datos para actualizar la propiedad
    data = {
        "address": "La elsa",
        "price": 160000.00,
        "size": 1300,
        "description": "Lejos.",
        "property_type": "house",
        "bedrooms": 3,
        "bathrooms": 2,
        "parking_spaces": 2,
        "year_built": 2001,
        "is_furnished": True
    }

    # Realizar la solicitud PUT
    url = reverse('/api/properties/', args=[property_instance.id])  # 
    response = client.put(url, data, format='json')
    
    assert response.status_code == status.HTTP_200_OK
    assert response.data['address'] == "La elsa"

@pytest.mark.django_db
def test_property_delete_view(client):
    # Crear un usuario
    User = get_user_model()
    user = User.objects.create_user(username="testuser", password="testpass")
    
    # Autenticación del usuario
    client.login(username="testuser", password="testpass")

    # Crear una propiedad
    property_instance = Property.objects.create(
        address="La elsa",
        price=150000.00,
        size=1200,
        description="A nice house.",
        property_type="house",
        bedrooms=3,
        bathrooms=2,
        parking_spaces=2,
        year_built=2000,
        is_furnished=True
    )

    # Realizar la solicitud DELETE
    url = reverse('/api/properties/', args=[property_instance.id])  # 
    response = client.delete(url)
    
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Property.objects.filter(id=property_instance.id).count() == 0
