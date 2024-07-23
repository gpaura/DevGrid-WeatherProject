from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import json
import datetime
import aiohttp
import asyncio
from django.conf import settings
from .serializers import WeatherRequestSerializer

class WeatherData:
    def __init__(self):
        self.data = {}

    def add_entry(self, request_id, city_id, temperature, humidity):
        if request_id not in self.data:
            self.data[request_id] = {
                'datetime': datetime.datetime.now().isoformat(),
                'cities': {}
            }
        self.data[request_id]['cities'][city_id] = {
            'temperature': temperature,
            'humidity': humidity
        }

    def get_progress(self, request_id):
        if request_id not in self.data:
            return None
        return len(self.data[request_id]['cities']) / len(settings.CITY_IDS) * 100

weather_data = WeatherData()

class WeatherView(APIView):
    async def fetch_weather(self, city_id):
        async with aiohttp.ClientSession() as session:
            async with session.get('http://api.openweathermap.org/data/2.5/weather', params={
                'id': city_id,
                'appid': settings.OPEN_WEATHER_API_KEY,
                'units': 'metric'
            }) as response:
                result = await response.json()
                return result

    def post(self, request):
        serializer = WeatherRequestSerializer(data=request.data)
        if serializer.is_valid():
            request_id = serializer.validated_data['id']
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            results = loop.run_until_complete(asyncio.gather(*[
                self.fetch_weather(city_id) for city_id in settings.CITY_IDS
            ]))

            for result in results:
                city_id = result['id']
                temperature = result['main']['temp']
                humidity = result['main']['humidity']
                weather_data.add_entry(request_id, city_id, temperature, humidity)
            
            return Response({'status': 'data collected', 'id': request_id}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        request_id = request.query_params.get('id')
        progress = weather_data.get_progress(request_id)
        if progress is None:
            return Response({'error': 'ID not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'progress': progress}, status=status.HTTP_200_OK)

