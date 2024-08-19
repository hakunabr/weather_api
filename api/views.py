import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings

# in this case we will not use a viewset, but a function based view, since the api will
# only return weather information, not delete, update or create
# decided to split functions in smaller ones to make it easier to modify and test
@api_view(['GET'])
def weather_view(request):
    city_name = request.query_params.get('city_name')
    if not city_name:
        return Response({'error': 'city_name query parameter is required'}, status=400)
    coords = get_city_coords(city_name)
    return get_weather_info(coords)

def get_city_coords(city_name):
    api_key = settings.API_KEY
    city_info_url = 'http://api.openweathermap.org/geo/1.0/direct?q={}&limit=1&appid={}'.format(city_name, api_key)
    coords_response = requests.get(city_info_url)
    city_coods = (coords_response.json()[0]['lat'], coords_response.json()[0]['lon'])
    return city_coods

def get_weather_info(coords):
    weather_url = 'https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&appid={}'.format(city_coods[0], city_coods[1], api_key)
    weather_response = requests.get(weather_url)
    return Response(weather_response.json())