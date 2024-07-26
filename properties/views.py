from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Property
from .serializers import PropertyDetailSerializer, PropertyListSerializer
from .services import PropertyService


class PropertyListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        service = PropertyService()
        properties = service.list_properties()
        paginator = PageNumberPagination()
        paginated_properties = paginator.paginate_queryset(properties, request)
        serializer = PropertyListSerializer(paginated_properties, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        service = PropertyService()
        serializer = PropertyDetailSerializer(data=request.data)
        if serializer.is_valid():
            property = service.create_property(serializer.validated_data)
            return Response(
                PropertyDetailSerializer(property).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        service = PropertyService()
        property = service.get_property(pk)
        serializer = PropertyDetailSerializer(property)
        return Response(serializer.data)

    def put(self, request, pk):
        service = PropertyService()
        serializer = PropertyDetailSerializer(data=request.data)
        if serializer.is_valid():
            property = service.update_property(pk, serializer.validated_data)
            return Response(PropertyDetailSerializer(property).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        service = PropertyService()
        property = service.get_property(pk)
        serializer = PropertyDetailSerializer(
            property,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            property = serializer.save()
            return Response(PropertyDetailSerializer(property).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        service = PropertyService()
        try:
            service.delete_property(pk)
            return Response(
                {
                    "message": (
                        f"Property with ID {pk} has been deleted successfully."
                    )
                },
                status=status.HTTP_204_NO_CONTENT,
            )
        except Property.DoesNotExist:
            return Response(
                {"detail": "Property not found."},
                status=status.HTTP_404_NOT_FOUND
            )
