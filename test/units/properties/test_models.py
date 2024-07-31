import pytest
from django.utils import timezone
from properties.models import Property

@pytest.mark.django_db
def test_property_creation():
    # Crear una instancia de Property
    property = Property.objects.create(
        address="123 Main St",
        price=100000.00,
        size=100,
        description="A beautiful house.",
        property_type="casa",
        bedrooms=3,
        bathrooms=2,
        parking_spaces=1,
        year_built=2000,
        is_furnished=True
    )
    
    # Verificar que la propiedad fue creada correctamente
    assert property.address == "123 Main St"
    assert property.price == 100000.00
    assert property.size == 100
    assert property.description == "A beautiful house."
    assert property.property_type == "casa"
    assert property.bedrooms == 3
    assert property.bathrooms == 2
    assert property.parking_spaces == 1
    assert property.year_built == 2000
    assert property.is_furnished is True

@pytest.mark.django_db
def test_property_str_method():
    # Crear una instancia de Property
    property = Property.objects.create(
        address="456 Elm St",
        price=150000.00,
        size=120,
        description="Another beautiful house.",
        property_type="apto",
        bedrooms=4,
        bathrooms=3,
        parking_spaces=2,
        year_built=2010,
        is_furnished=False
    )
    
    # Verificar el método __str__
    assert str(property) == "456 Elm St"