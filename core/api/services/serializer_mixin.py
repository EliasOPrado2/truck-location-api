from core.models.route_model import Route
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from rest_framework import serializers
from core.api import exceptions
from core.models import (
    TruckDriver, 
    DestinationCoordinate, 
    OriginCoordinate,
    Route,
)

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

        if self.Meta.model == DestinationCoordinate:
            # remove 'origin' from validated_data.
            origin_id = validated_data.pop('origin')
            address = [x for x in validated_data.values() if x.strip()]
            validated_data['origin'] = origin_id
            clean_address = ' '.join(address)
        
        if self.Meta.model == OriginCoordinate:
            address = [x for x in validated_data.values() if x.strip()]
            clean_address = ' '.join(address)

        try:
            location = geolocator.geocode(clean_address)
            validated_data['longitude'] = location.longitude
            validated_data['latitude'] = location.latitude
            
        except AttributeError:
            raise exceptions.InvalidAddress()

        # get truck-driver id from url.
        truck_driver_id = self.context["view"].kwargs.get("truckdrivers_pk")
        truck_driver = TruckDriver.objects.get(id=truck_driver_id)
        validated_data['truck_driver'] = truck_driver

        data = self.Meta.model.objects.create(**validated_data)

        if self.Meta.model == DestinationCoordinate:
            print("DESTINATION DATA ---->", data.pk)
            print("ORIGIN ID ---->",origin_id)
            # distance_in_km = geodesic(location1_coord, location2_coord).km

            try:
                # need to check if the origin id already has a destination.
                if OriginCoordinate.objects.get(id=origin_id.pk, destination__isnull=True): # <---- something wrong.
                    print("----------BATEU AQUI --------------")
                    destination_data = data
                    # if not send this 'destination_id' from 'data' to the origin query and save.
                    origin_queryset = OriginCoordinate.objects.get(id=origin_id.pk)
                    origin_queryset.destination = DestinationCoordinate.objects.get(id=destination_data.pk)
                    origin_queryset.save()
                    print("----------BATEU AQUI 2 --------------")
                    # get this origin, destination, calculate the distance and send to 'Route' and save.
                    origin_coord = (origin_coord.latitude, origin_coord.longitude)
                    print("ORIGIN COORD --->", origin_coord)
                    destination_coord = (destination_coord.latitude, destination_coord.longitude)
                    print("DESTINATION COORD --->", destination_coord)
                    print("----------BATEU AQUI 3--------------")
                    distance_in_km = geodesic(origin_coord, destination_coord).km
                    print("DISTANCE --->", distance_in_km)
                    route = Route.objects.create(
                        origin=origin_id, 
                        destination=destination_data, 
                        distance=distance_in_km, is_active=True
                    )
                    print("ROUTE -->", route)
                    return destination_data
            # add proper exception name.
            except Exception:
                # create an exception defining that the origin already has a destination.
                raise exceptions.OriginAlreadyPopulated()

            
        return data

# FIX THE EXCEPTION ERROR AND SEND THE DATA TO ROUTE

# SET ROUTE TO TRUCK DRIVER AS NESTED VALUE OR "NESTED URL"

# SET HOW MANY TRUCKS HAS PASSED IN THE TERMINAL BASED ON THE CREATED_AT AND NUMBER OF ROUTERS + IS_ACTIVE.

# DO THE TESTS.

