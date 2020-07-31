# vehicles/views.py

from rest_framework import permissions
from shared.permissions import IsOwnerOrReadOnly
from .models import Vehicle
from .serializers import VehicleSerializer
from rest_framework import status, viewsets


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    
    permission_classes = [
        IsOwnerOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly,
    ]

    def perform_create(self, serializer):
        # set user to the logged in user
        serializer.save(user=self.request.user)