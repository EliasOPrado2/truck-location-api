from geopy.geocoders import Nominatim
from decouple import config
from core.api import exceptions
from rest_framework import serializers
from core.models import Address


class AddressSerializer(serializers.ModelSerializer):
    """
    Serializes the Address data.

    :param ModelSerializer (SerializerMetaclass): Serialize model objects.
    """
    GEOLOCATOR = Nominatim(user_agent=config('USER_AGENT'))

    class Meta:
        model = Address
        fields = [
            'id', 
            'address', 
            'neighborhood', 
            'city', 
            'state', 
            'postcode', 
            'country', 
            'latitude',
            'longitude', 
        ]
        
        extra_kwargs = {
            "latitude": {"read_only": True},
            "longitude": {"read_only": True},
        }

    def set_location(self, data):
        address = [x for x in data.values() if x.strip()]
        clean_address = ' '.join(address)
        return self.GEOLOCATOR.geocode(clean_address)

    def create(self, validated_data):
        try:
            location = self.set_location(validated_data)
            validated_data['longitude'] = location.longitude
            validated_data['latitude'] = location.latitude
        except AttributeError:
            raise exceptions.InvalidAddress()

        return Address.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        try:
            location = self.set_location(validated_data)
            instance.longitude = location.longitude
            instance.latitude = location.latitude
        except AttributeError:
            raise exceptions.InvalidAddress()

        instance.address = validated_data.get('address', instance.address)
        instance.neighborhood = validated_data.get('neighborhood', instance.neighborhood)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.postcode = validated_data.get('postcode', instance.postcode)
        instance.country = validated_data.get('country', instance.country)
        
        return instance
