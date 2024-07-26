from django.db import models


class WeatherData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
