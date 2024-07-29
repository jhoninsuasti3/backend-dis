# properties/urls.py
from django.urls import path

from .views import(
    PropertyDetailView,
    PropertyListView,
    BulkPropertyCreateView,
)

urlpatterns = [
    path(
        'properties/',
        PropertyListView.as_view(),
        name='property-list'
    ),
    path(
        'properties/<int:pk>/',
        PropertyDetailView.as_view(),
        name='property-detail'
    ),
    path(
        'bulk_create/',
        BulkPropertyCreateView.as_view(),
        name='bulk_create_properties'
    ),
]
