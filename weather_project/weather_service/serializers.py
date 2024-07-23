from rest_framework import serializers

class WeatherRequestSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
