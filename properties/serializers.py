# serializers.py
from rest_framework import serializers

from .models import Property


class PropertyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ["id","address", "price", "size"]


class PropertyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"
        read_only_fields = ("id",)  # El campo id solo será de lectura


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['address', 'price', 'size', 'description', 'property_type']

class BulkPropertySerializer(serializers.ListSerializer):
    child = PropertySerializer()

    def create(self, validated_data):
        properties = [Property(**item) for item in validated_data]
        return Property.objects.bulk_create(properties)