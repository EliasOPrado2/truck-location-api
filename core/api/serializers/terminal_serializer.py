from rest_framework import serializers
from django.db.models import Count


class TerminalSerializer(serializers.Serializer):

    trucks_per_day = serializers.IntegerField()
    trucks_per_week = serializers.IntegerField()
    trucks_per_month = serializers.IntegerField()
    