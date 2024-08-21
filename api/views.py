import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.core.cache import cache

# in this case we will not use a viewset, but a function based view, since the api will
# only return weather information
@api_view(['GET'])
def weather_view(request):
    api_key = settings.API_KEY
    print(request.query_params)
    city_name = request.query_params.get('city_name')
    period = request.query_params.get('period')
    if not city_name:
        return Response({'error': 'city_name query parameter is required'}, status=400)
    
    if period == 'week':
        period = 'next7days'
    elif period == 'month':
        period = 'next30days'
    else:
        period = 'today'
    
    # creates a key for the city_name and period, and checks if said key is in chahe
    # if so, returns the cached version
    cache_key = f'weather_{city_name}_{period}'
    cached_response = cache.get(cache_key)
    if cached_response:
        return Response(cached_response)
    
    call_string = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{}/{}?key={}'.format(city_name, period, api_key)
    response = requests.get(call_string)

    # if its not cached, the above lines will fetch the data and then, if it receives a valid response
    # it will cache the response for 12 hours
    if response.status_code == 200:
        data = response.json()
        cache.set(cache_key, data, timeout=3600*12)
        return Response(data)
    else:
        return Response({'error': 'An error occurred while trying to get weather information'}, status=500)