# properties/tests/test_models.py
import pytest

from properties.models import Property


@pytest.mark.django_db
def test_property_creation():
    property = Property.objects.create(
        address="Calle 100 # 4",
        price=18000000.00,
        size=85,
        description="Casa destino"
    )
    assert isinstance(property, Property)
    assert str(property) == property.address


@pytest.mark.django_db
def test_property_price():
    property = Property.objects.create(
        address="Calle 100 # 4",
        price=18000000.00,
        size=85,
        description="Casa destino"
    )
    assert property.price == 18000000.00


@pytest.mark.django_db
def test_property_size():
    property = Property.objects.create(
        address="Calle 100 # 4",
        price=18000000.00,
        size=85,
        description="Casa destino"
    )
    assert property.size == 85
