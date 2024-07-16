from django.urls import path
from .views import PropertyListCreate, PropertyRetrieveUpdateDestroy

urlpatterns = [
    path('properties/', PropertyListCreate.as_view(), name='property-list-create'),
    path('properties/<int:pk>/', PropertyRetrieveUpdateDestroy.as_view(), name='property-retrieve-update-destroy'),
]
