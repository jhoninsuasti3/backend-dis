# properties/tests/test_views.py
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


def test_list_properties(api_client, property_instance):
    url = reverse("property-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert "results" in response.data
    assert len(response.data["results"]) > 0


def test_create_property(api_client):
    url = reverse("property-list")
    data = {
        "address": "Calle 200 # 5",
        "price": "20000000.00",
        "size": 90,
        "description": "Nueva casa",
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["address"] == data["address"]


def test_get_property(api_client, property_instance):
    url = reverse("property-detail", args=[property_instance.pk])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["address"] == property_instance.address


def test_update_property(api_client, property_instance):
    url = reverse("property-detail", args=[property_instance.pk])
    data = {"price": "25000000.00", "size": 95}
    response = api_client.put(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["price"] == data["price"]
    assert response.data["size"] == data["size"]


def test_delete_property(api_client, property_instance):
    url = reverse("property-detail", args=[property_instance.pk])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Property.objects.count() == 0
