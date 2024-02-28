from django.urls import path
from . import views

urlpatterns = [
    path('api/data/', views.get_latest_office_data, name='office_data_api'),
    path('set_temp/', views.set_temp, name='handle_weather_data'),
    path("", views.office_main_view, name="office_main"),
]
