from django.test import TestCase
from rest_framework.test import APITestCase

# Create your tests here.
class WeatherViewTests(APITestCase):

    def test_weather_view(self):
        response = self.client.get('/api/weather/?city_name=Londrina&period=week')
        self.assertEqual(response.status_code, 200)
    
    def test_weather_view_no_city_name(self):
        response = self.client.get('/api/weather/')
        self.assertEqual(response.status_code, 400)
