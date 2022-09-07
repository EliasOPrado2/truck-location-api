from rest_framework import viewsets

from core.api.serializers import AddressSerializer
from core.models import Address


class AddressViewSet(viewsets.ModelViewSet):
    """
    ViewSete do display Address data.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
