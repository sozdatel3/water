from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('calculate_simulation/', views.calculate_simulation,
         name='calculate_simulation'),
    path('room_temp/', views.room_view, name="room"),
]
