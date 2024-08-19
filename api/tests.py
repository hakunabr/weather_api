from django.test import TestCase
from rest_framework.test import APITestCase

# Create your tests here.
class WeatherViewTests(APITestCase):

    def test_weather_view(self):
        response = self.client.get('/api/weather/?city_name=Londrina')
        print(response.json())
