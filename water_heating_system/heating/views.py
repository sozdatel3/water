# Create your views here.
from django.http import JsonResponse
# from .simulation import simulate_heating_process
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .forms import ContainerForm
from .models import Container, Room
import json


def room_view(request):
    try:
        room = Room.objects.first()  # Получаем первое помещение из базы данных
    except Exception:
        room = None
    # Проверяем, существует ли помещение
    if not room:
        # Если помещение не существует, создаем новое с заданными параметрами
        room = Room(length=2.0, width=1.0,
                    wall_thickness=0.1, temperature=25.0)
        # room.save()  # Сохраняем новое помещение в базу данных
    context = {
        'room': room
    }
    return render(request, 'heating/room.html', context)


def main_page(request):
    form = ContainerForm()
    return render(request, "heating/simulation_form.html", {'form': form})


@csrf_exempt
def calculate_simulation(request):
    if request.method != 'POST':
        # Если это не POST запрос, возвращаем пустой JSON объект
        return JsonResponse({})
    # Получаем данные из запроса
    data = json.loads(request.body)
    volume = data.get('volume')
    initial_temperature = data.get('initial_temperature')
    target_temperature = data.get('target_temperature')
    efficiency = data.get('efficiency')
    power = data.get("power")
    print(volume, initial_temperature,
          target_temperature, efficiency, power)
    # Преобразуем строки в числа
    volume = float(volume) if volume else 0
    initial_temperature = float(
        initial_temperature) if initial_temperature else 0
    target_temperature = float(
        target_temperature) if target_temperature else 0
    efficiency = float(efficiency) if efficiency else 100

    power = float(efficiency) if power else 100

    # Выполняем симуляцию
    time_spent, energy_spent = simulate_heating_process(
        volume, initial_temperature, target_temperature, efficiency, power
    )

    # Возвращаем результаты
    return JsonResponse({
        'time_spent': time_spent,
        'energy_spent': energy_spent
    })


def simulate_heating_process(volume, initial_temp, target_temp, efficiency, power):
    T1 = initial_temp  # температура холодной воды в °C
    T2 = target_temp  # температура нагретой воды в °C
    V = volume  # объем или масса воды в литрах (или кг)
    c = 4.187  # удельная теплоемкость воды в кДж/(кг·°C)

    # Рассчитываем расход электроэнергии в кВт·ч, учитывая КПД
    energy_kWh = ((T2 - T1) * V * c) / (efficiency/100)*0.027777777777

    # Рассчитываем время в часах, необходимое для нагрева
    time_hours = energy_kWh / power

    return energy_kWh, time_hours
