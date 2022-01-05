from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from profiles.models import Profile
from profiles.api.serializers import ProfileSerializer
from profiles.api.permissions import IsOwnProfileOrReadOnly


class ProfileRUAPIView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]
    lookup_field = 'uuid'