from rest_framework import viewsets
from core.models import TruckDriver
from core.api.serializers import TruckDriverSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TruckDriverViewSet(viewsets.ModelViewSet):
    # add comment
    queryset = TruckDriver.objects.all()
    serializer_class = TruckDriverSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_loaded', 'has_truck']