from .models import Property


class PropertyService:
    def list_properties(self):
        return Property.objects.all()

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
