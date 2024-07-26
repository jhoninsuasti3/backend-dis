# serializers.py
from rest_framework import serializers

from .models import Property


class PropertyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ["address", "price", "size"]


class PropertyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"
        read_only_fields = ("id",)  # El campo id solo será de lectura
