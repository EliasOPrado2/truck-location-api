from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from rest_framework import serializers
from core.api import exceptions
from core.models import TruckDriver
from decouple import config


class CoordinatesSerializerMixin(serializers.ModelSerializer):
    """
    Serializer mixin to be used as inheritance into others serialzers such as
    DestinationCoordinateSerializer and OriginCoordinateSerializer that have 
    similar structure.

    :param serializers (module): Inherit a set of serialization structures.
    """
    def create(self, validated_data):
        """
        Handles the data creation from the current serializer.

        :param validated_data (dict): validated json data from request.
        :raises exceptions.InvalidAddress (type): Exception raized when the address does not exist.
        :return (obj): Return a dict from the current created object.
        """
        geolocator = Nominatim(user_agent=config('USER_AGENT'))
        address = [x for x in validated_data.values() if x.strip()]
        clean_address = ' '.join(address)

        try:
            location = geolocator.geocode(clean_address)
            validated_data['longitude'] = location.longitude
            validated_data['latitude'] = location.latitude
            
        except AttributeError:
            raise exceptions.InvalidAddress()

        # get truck-driver id from url request.
        truck_driver_id = self.context["view"].kwargs.get("truckdrivers_pk")
        truck_driver = TruckDriver.objects.get(id=truck_driver_id)
        validated_data['truck_driver'] = truck_driver

        return self.Meta.model.objects.create(**validated_data)
