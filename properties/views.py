from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics


from .models import Property
from .serializers import(
    PropertyDetailSerializer,
    PropertyListSerializer,
    BulkPropertySerializer,
    PropertySerializer
)
from .services import PropertyService
from drf_yasg.utils import swagger_auto_schema
from utils.generic_decorators import GenerateSwagger



@GenerateSwagger(swagger_auto_schema)
class PropertyListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        service = PropertyService()
        # Extraer parámetros de consulta y construir el diccionario de filtros
        filters = {
            'property_type': request.query_params.get('property_type', None),
            'min_price': request.query_params.get('min_price', None),
            'max_price': request.query_params.get('max_price', None),
            'size': request.query_params.get('size', None),
        }
        # Eliminar filtros con valores None
        filters = {key: value for key, value in filters.items() if value is not None}
        properties = service.list_properties(**filters)
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


@GenerateSwagger(swagger_auto_schema)
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

# Add various items
@GenerateSwagger(swagger_auto_schema)
class BulkPropertyCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        serializer = BulkPropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
