import geopy.distance
from rest_framework import serializers
from core.models import TruckDriver

class TruckDriverSerializer(serializers.ModelSerializer):
    # add comment
    class Meta:
        model = TruckDriver
        fields = [
            'id', 
            'name', 
            'age', 
            'sex', 
            'has_truck', 
            'cnh_type', 
            'is_loaded', 
            'truck_type'
        ]
