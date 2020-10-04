from django.urls import path
from weather import views

urlpatterns = [
    path('', views.home, name="utility_home"),
    path('weather/', views.index, name="weather_home"),
    path('delete/<city_name>/', views.delete_city, name="delete_city"),
]
