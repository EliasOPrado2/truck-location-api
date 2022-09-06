from rest_framework import serializers
from django.db.models import Count



class TerminalSerializer(serializers.Serializer):

    trucks_per_day = serializers.IntergerField()
    trucks_per_week = serializers.IntergerField()
    trucks_per_month = serializers.IntergerField()

    