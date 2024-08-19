from .views import weather_view
from django.urls import path, include 


urlpatterns = [
    path('weather/', weather_view, name='weather_view'),
]