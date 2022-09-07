from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from core.api.serializers import TruckDriverSerializer
from core.models import TruckDriver


class TruckDriverViewSet(viewsets.ModelViewSet):
    """
    ViewSet to display TruckDriver data and handle its filters.
    """
    queryset = TruckDriver.objects.all()
    serializer_class = TruckDriverSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["is_loaded", "has_truck"]
