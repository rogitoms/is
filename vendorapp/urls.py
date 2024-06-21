from django.urls import path
from clientapp.views import ClientFirearmsView

urlpatterns = [
    path('firearms', ClientFirearmsView.as_view({'get': 'get_client_firearms'}), name='vendor_firearms'),
    path('firearms/<int:id>', ClientFirearmsView.as_view({'get': 'details'}), name='vendor_firearm_details'),
]