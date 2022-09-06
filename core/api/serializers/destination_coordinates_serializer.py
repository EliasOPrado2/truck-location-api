from geopy.distance import geodesic
from geopy.geocoders import Nominatim

from core.api import exceptions
from core.api.services.serializer_mixin import CoordinatesSerializerMixin
from rest_framework import serializers
from core.models import DestinationCoordinate, TruckDriver


""" 
***** Falar sobre  duvida na criação de origin e destination *****
"""

class DestinationCoordiateSerializer(CoordinatesSerializerMixin):
    """
    Serializes the DestinationCoordinate data.

    :param CoordinatesSerializerMixin (ModelSerializer): Holds customized methods from ModelSerializer.
    """
    class Meta:
        model = DestinationCoordinate
        fields = [
            'id', 
            'truck_driver', 
            'address', 
            'neighborhood', 
            'city', 
            'state', 
            'postcode', 
            'country', 
            'longitude', 
            'latitude',
            'origin',
        ]
        
        extra_kwargs = {
            "truck_driver": {"read_only": True},
            "latitude": {"read_only": True},
            "longitude": {"read_only": True},
        }
