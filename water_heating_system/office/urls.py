from django.urls import path
from . import views

urlpatterns = [
    path("", views.office_main_view, name="office_main"),
    path('set_temp/', views.handle_weather_data, name='handle_weather_data'),
]
