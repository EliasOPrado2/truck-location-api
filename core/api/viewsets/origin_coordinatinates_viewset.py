from rest_framework import viewsets
from core.models import OriginCoordinate
from core.api.serializers import OriginCoordiateSerializer
from core.api.services.viewset_mixin import CoordinatesViewSetMixin

class OriginCoordinateViewSet(CoordinatesViewSetMixin):
    # add comment
    model = OriginCoordinate
    queryset = OriginCoordinate.objects.all()
    serializer_class = OriginCoordiateSerializer