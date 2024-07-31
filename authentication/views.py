from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny  # Permitir acceso sin autenticación
from .serializers import RegisterSerializer
from drf_yasg.utils import swagger_auto_schema
from utils.swagger_config import user_create_request_example, user_create_response_example, user_create_error_response_example


class RegisterView(APIView):
    permission_classes = [AllowAny]  # Permitir acceso sin autenticación

    @swagger_auto_schema(
        request_body=user_create_request_example,
        responses={
            201: user_create_response_example,
            400: user_create_error_response_example,
        }
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
