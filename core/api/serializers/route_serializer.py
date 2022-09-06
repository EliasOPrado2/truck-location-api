from geopy.distance import geodesic
from rest_framework import serializers
from core.models import Route, TruckDriver, Address


class RouteSerializer(serializers.ModelSerializer):

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

    def create(self, validated_data):
        truck_driver_id = self.context["view"].kwargs.get("truckdrivers_pk")
        truck_driver = TruckDriver.objects.get(id=truck_driver_id)
        validated_data['truck_driver'] = truck_driver

        # not allow similar address for both origin and distance.

        # get coordinates from origin and destination and calculate distance.
        origin = None
        destination = None

        origin_coord = None
        destination_coord = None

        distance_in_km = geodesic(origin_coord, destination_coord).km

        return Route.objects.create(**validated_data)

    def to_representation(self, instance):

        return super(RouteSerializer, self).to_representation(instance)