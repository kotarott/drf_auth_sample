from django.urls import path, include
from profiles.api.views import ProfileRUAPIView


urlpatterns = [
    path('<str:uuid>/', ProfileRUAPIView.as_view(), name='profile-detail'),
]
