from django.contrib import admin
from typing import Any
from django.urls import include, path, re_path
from core.doc_swagger import *

urlpatterns: list[Any] = [
    # DOCUMENTATION ENDPOINTS #
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
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