from django.urls import path

from adminApp.views import ClientView

urlpatterns = [
    path('clients', ClientView.as_view({'get':'list'}), name='clients'),
]