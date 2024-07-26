from django.urls import path
from .views import CollectWeatherDataView, GetWeatherDataProgressView

urlpatterns = [
    path("collect/", CollectWeatherDataView.as_view(), name="collect_weather_data"),
    path(
        "progress/<str:user_defined_id>/",
        GetWeatherDataProgressView.as_view(),
        name="get_weather_data_progress",
    ),
]
