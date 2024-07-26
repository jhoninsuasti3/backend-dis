# properties/tests/test_serializers.py
import pytest

from properties.models import Property
from properties.serializers import PropertyDetailSerializer


@pytest.mark.django_db
def test_property_serializer():
    property = Property.objects.create(
        address="Calle 100 # 4",
        price=18000000.00,
        size=85,
        description="Casa destino"
    )
    serializer = PropertyDetailSerializer(instance=property)
    data = serializer.data
    assert set(data.keys()) == {
        "id",
        "address",
        "price",
        "size",
        "description"
    }
    assert data["address"] == property.address
    assert data["price"] == str(property.price)
    assert data["size"] == property.size
    assert data["description"] == property.description
