import os
import requests
import asyncio
import aiohttp
from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.response import Response
from .models import WeatherData
from .serializers import WeatherDataSerializer


API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
CITY_IDS = [
    3439525,
    3439781,
    3440645,
    3442098,
    3442778,
    3443341,
    3442233,
    3440781,
    3441572,
    3441575,
    3443207,
    3442546,
    3441287,
    3441242,
    3441686,
    3440639,
    3441354,
    3442057,
    3442585,
    3442727,
    3439705,
    3441890,
    3443411,
    3440054,
    3441684,
    3440711,
    3440714,
    3440696,
    3441894,
    3443173,
    3441702,
    3442007,
    3441665,
    3440963,
    3443413,
    3440033,
    3440034,
    3440571,
    3443025,
    3441243,
    3440789,
    3442568,
    3443737,
    3440771,
    3440777,
    3442597,
    3442587,
    3439749,
    3441358,
    3442980,
    3442750,
    3443352,
    3442051,
    3441442,
    3442398,
    3442163,
    3443533,
    3440942,
    3442720,
    3441273,
    3442071,
    3442105,
    3442683,
    3443030,
    3441011,
    3440925,
    3440021,
    3441292,
    3480823,
    3440379,
    3442106,
    3439696,
    3440063,
    3442231,
    3442926,
    3442050,
    3440698,
    3480819,
    3442450,
    3442584,
    3443632,
    3441122,
    3441475,
    3440791,
    3480818,
    3439780,
    3443861,
    3440780,
    3442805,
    7838849,
    3440581,
    3440830,
    3443756,
    3443758,
    3443013,
    3439590,
    3439598,
    3439619,
    3439622,
    3439652,
    3439659,
    3439661,
    3439725,
    3439748,
    3439787,
    3439831,
    3439838,
    3439902,
    3440055,
    3440076,
    3440394,
    3440400,
    3440541,
    3440554,
    3440577,
    3440580,
    3440596,
    3440653,
    3440654,
    3440684,
    3440705,
    3440747,
    3440762,
    3440879,
    3440939,
    3440985,
    3441074,
    3441114,
    3441377,
    3441476,
    3441481,
    3441483,
    3441577,
    3441659,
    3441674,
    3441803,
    3441954,
    3441988,
    3442058,
    3442138,
    3442206,
    3442221,
    3442236,
    3442238,
    3442299,
    3442716,
    3442766,
    3442803,
    3442939,
    3443061,
    3443183,
    3443256,
    3443280,
    3443289,
    3443342,
    3443356,
    3443588,
    3443631,
    3443644,
    3443697,
    3443909,
    3443928,
    3443952,
    3480812,
    3480820,
    3480822,
    3480825,
]


async def fetch_weather(session, city_id):
    url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}&units=metric"
    async with session.get(url) as response:
        return await response.json()


async def fetch_all_weather_data():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for city_id in CITY_IDS:
            tasks.append(fetch_weather(session, city_id))
        weather_data = await asyncio.gather(*tasks)
    return weather_data


class CollectWeatherDataView(views.APIView):
    async def post(self, request, *args, **kwargs):
        user_defined_id = request.data.get("user_defined_id")
        if WeatherData.objects.filter(user_defined_id=user_defined_id).exists():
            return Response(
                {"error": "This ID already exists."}, status=status.HTTP_400_BAD_REQUEST
            )

        weather_data = await fetch_all_weather_data()

        weather_data_objects = []
        for data in weather_data:
            if "main" in data and "id" in data:
                weather_data_objects.append(
                    WeatherData(
                        user_defined_id=user_defined_id,
                        city_id=data["id"],
                        temperature_celsius=data["main"]["temp"],
                        humidity=data["main"]["humidity"],
                    )
                )
        WeatherData.objects.bulk_create(weather_data_objects)

        return Response(
            {"status": "Weather data collected successfully"},
            status=status.HTTP_201_CREATED,
        )


class GetWeatherDataProgressView(views.APIView):
    def get(self, request, user_defined_id, *args, **kwargs):
        weather_data_count = WeatherData.objects.filter(
            user_defined_id=user_defined_id
        ).count()
        total_cities = len(CITY_IDS)
        progress_percentage = (weather_data_count / total_cities) * 100
        return Response({"progress": f"{progress_percentage:.2f}%"})
