# urls.py
from django.urls import path
from .views import FirearmViewSet

urlpatterns = [
    path('firearms', FirearmViewSet.as_view({'get': 'list_firearms', 'post': 'create_firearm'}), name='firearms'),
    path('firearms/<int:id>', FirearmViewSet.as_view({'get': 'retrieve_firearm'}), name='firearm_details'),
]
