from .models import Property


class PropertyService:
    def list_properties(self, **filters):
        # Aplicar filtros dinámicamente
        properties = Property.objects.all()
        if 'property_type' in filters:
            properties = properties.filter(property_type=filters['property_type'])
        if 'min_price' in filters:
            properties = properties.filter(price__gte=filters['min_price'])
        if 'max_price' in filters:
            properties = properties.filter(price__lte=filters['max_price'])
        if 'size' in filters:
            properties = properties.filter(size=filters['size'])
        if 'antiguedad' in filters:
            properties = properties.filter(antiguedad=filters['antiguedad'])
        return properties

    def get_property(self, pk):
        return Property.objects.get(pk=pk)

    def create_property(self, validated_data):
        return Property.objects.create(**validated_data)

    def update_property(self, pk, validated_data):
        property = Property.objects.get(pk=pk)
        for attr, value in validated_data.items():
            setattr(property, attr, value)
        property.save()
        return property

    def delete_property(self, pk):
        property = Property.objects.get(pk=pk)
        property.delete()
