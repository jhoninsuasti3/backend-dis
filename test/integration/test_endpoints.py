# properties/tests/test_endpoints.py
import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from properties.models import Property


@pytest.fixture
def user():
    User = get_user_model()
    user = User.objects.create_user(username="testuser", password="testpass")
    return user


@pytest.fixture
def api_client(user):
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    client.credentials(HTTP_AUTHORIZATION="Bearer " + access_token)
    return client


@pytest.fixture
def property_instance():
    return Property.objects.create(
        address="Calle 100 # 4",
        price=18000000.00,
        size=85,
        description="Casa destino"
    )


def test_property_endpoints(api_client, property_instance):
    # Test list properties
    url = reverse("property-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert "results" in response.data
    assert len(response.data["results"]) > 0

    # Test create property
    data = {
        "address": "Calle 200 # 5",
        "price": "20000000.00",
        "size": 90,
        "description": "Nueva casa",
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["address"] == data["address"]

    # Test get property
    property_id = response.data["id"]
    url = reverse("property-detail", args=[property_id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["address"] == data["address"]

    # Test update property
    updated_data = {"price": "25000000.00", "size": 95}
    response = api_client.put(url, updated_data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["price"] == updated_data["price"]
    assert response.data["size"] == updated_data["size"]

    # Test delete property
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Property.objects.count() == 0
