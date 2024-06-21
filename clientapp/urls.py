from django.urls import path

from clientapp.views import ClientApplicationView, ClientFirearmsView, ClientProfileView

urlpatterns = [
    path('profile', ClientProfileView.as_view({'get': 'get_profile'}), name='get_profile'),
    path('update-profile', ClientProfileView.as_view({'post': 'update'}), name='update_profile'),

    path('applications', ClientApplicationView.as_view({'get': 'get_applications'}), name='get_applications'),
    path('apply', ClientApplicationView.as_view({'post': 'create'}), name='apply'),
    path('renew', ClientApplicationView.as_view({'post': 'renew'}), name='apply-renew'),

    path('firearms', ClientFirearmsView.as_view({'get': 'get_client_firearms'}), name='get_firearms'),
    path('firearms/<int:id>', ClientFirearmsView.as_view({'get': 'details'}), name='firearm_details'),

]