from rest_framework import viewsets
from core.models import DestinationCoordinate
from core.api.serializers import DestinationCoordiateSerializer
from core.api.services.viewset_mixin import CoordinatesViewSetMixin


class DestinationCoordinateViewSet(CoordinatesViewSetMixin):
    # add comment
    model = DestinationCoordinate
    queryset = DestinationCoordinate.objects.all()
    serializer_class = DestinationCoordiateSerializer

