from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from typing import Any


schema_view = get_schema_view(
    openapi.Info(
        title="Mi API",
        default_version='v1',
        description="Descripción de la API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@miapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns: list[Any] = [
    # DOCUMENTATION ENDPOINTS #
    re_path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    #admin
    path(
        'admin/',
        admin.site.urls
    ),
    # AUTHENTICATION
    path(
        'api/auth/',
        include('authentication.urls')
    ),
    #PROPERTIES    
    path(
        'api/',
        include('properties.urls')
    ),   
]