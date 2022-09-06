from geopy.distance import geodesic
from django.db.models.functions import TruncMonth
from django.db.models import Count
from rest_framework import serializers
from core.api import exceptions
from core.models import Route, TruckDriver, Address


class RouteSerializer(serializers.ModelSerializer):
    """
    Serialize the Route model to JSON.

    :param ModelSerializer (SerializerMetaclass): Serialize model objects.
    :raises exceptions.NoSimilarAddress: Origin and destination should not be similar.
    :return (JSON): Route JSON object.
    """
    class Meta:
        model = Route
        fields = [
            'id', 
            'truck_driver', 
            'origin', 
            'destination', 
            'distance', 
            'is_active', 
            'created_at'
        ]
        extra_kwargs = {
            "truck_driver": {"read_only": True},
            "created_at": {"read_only": True},
            "distance": {"read_only": True},
        }
    def set_distance(self, validated_data):
        # get coordinates from origin and destination and calculate distance.
        # get origin and destination.
        origin = validated_data['origin']
        destination = validated_data['destination']

        # Do not allow similar address for both origin and distance.
        if origin == destination:
            raise exceptions.NoSimilarAddress()

        # get coordinates from origin and destination.
        origin_coord = (origin.latitude, origin.longitude)
        destination_coord = (destination.latitude, destination.longitude)

        # calculate distance from origin and destination coordinates.
        distance_in_km = geodesic(origin_coord, destination_coord).km

        return distance_in_km

    def create(self, validated_data):
        truck_driver_id = self.context["view"].kwargs.get("truckdrivers_pk")
        truck_driver = TruckDriver.objects.get(id=truck_driver_id)
        validated_data['truck_driver'] = truck_driver

        distance_in_km = self.set_distance(validated_data)
        
        # set distance and is_active.
        validated_data['distance'] = distance_in_km
        validated_data['is_active'] = True

        return Route.objects.create(**validated_data)

    def update(self, instance, validated_data):
        truck_driver_id = self.context["view"].kwargs.get("truckdrivers_pk")
        truck_driver = TruckDriver.objects.get(id=truck_driver_id)

        distance_in_km = self.set_distance(validated_data)

        instance.truck_driver = truck_driver
        instance.origin = validated_data['origin']
        instance.destination = validated_data['destination']
        instance.distance = distance_in_km

        # activate and deactivate distance in a query parameter.
        
        return super().update(instance, validated_data)

    def to_representation(self, instance):

        item = Route.objects.annotate(month=TruncMonth('created_at')).values('month').annotate(c=Count('id')).values('month', 'c') 
        print(item)
        origin = instance.origin
        destination = instance.destination
        data = {
            'id':instance.id,
            'truck_driver':instance.truck_driver.id,
            'origin':{
                'id': origin.id,
                'address': origin.address,
                'neighborhood':origin.neighborhood,
                'city':origin.city,
                'state':origin.state,
                'postcode':origin.postcode,
                'latitude':origin.latitude,
                'longitude': origin.longitude
            },
            'destination':{
                'id': destination.id,
                'address': destination.address,
                'neighborhood':destination.neighborhood,
                'city':destination.city,
                'state':destination.state,
                'postcode':destination.postcode,
                'latitude':destination.latitude,
                'longitude': destination.longitude
            },
            'distance': instance.distance, 
            'is_active': instance.is_active, 
            'created_at': instance.created_at,
        }
        return data
