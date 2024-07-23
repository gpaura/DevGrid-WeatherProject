from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
import json

class WeatherAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_post_weather(self):
        response = self.client.post(reverse('weather'), {'id': 'test123'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('data collected', json.loads(response.content).get('status'))

    def test_get_progress(self):
        self.client.post(reverse('weather'), {'id': 'test123'})
        response = self.client.get(reverse('weather') + '?id=test123')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('progress', json.loads(response.content))

