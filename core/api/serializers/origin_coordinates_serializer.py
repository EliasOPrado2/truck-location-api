import geopy.distance
from rest_framework import serializers
from core.api.services.serializer_mixin import CoordinatesSerializerMixin
from core.models import OriginCoordinate, TruckDriver

class OriginCoordiateSerializer(CoordinatesSerializerMixin):
    # add comment
    class Meta:
        model = OriginCoordinate
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
            'destination'
        ]
        
        extra_kwargs = {
            "truck_driver": {"read_only": True},
            "latitude": {"read_only": True},
            "longitude": {"read_only": True},
        }