# Create your views here.
from django.http import JsonResponse
# from .simulation import simulate_heating_process
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .forms import ContainerForm
from .models import Container
import json

# def simulate_heating(request):
#     if request.method == 'POST':
#         form = ContainerForm(request.POST)
#         if form.is_valid():

#             # Здесь будет логика симуляции и расчета потраченной энергии и времени
#             container = form.save(commit=False)

#             # Предположим, что симуляция происходит мгновенно и мы просто рассчитаем энергию и время
#             energy, time = simulate(container.volume, container.initial_temperature,
#                                     container.target_temperature, container.efficiency)

#             # Сохранение результатов для передачи в шаблон
#             results = {
#                 'energy': energy,
#                 'time': time,
#             }
#             return render(request, 'heating/results.html', {'form': form, 'results': results})
#     else:
#         form = ContainerForm()
#     return render(request, 'heating/simulation_form.html', {'form': form})


def main_page(request):
    form = ContainerForm()
    return render(request, "heating/simulation_form.html", {'form': form})


@csrf_exempt
def calculate_simulation(request):
    if request.method == 'POST':
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

    # Если это не POST запрос, возвращаем пустой JSON объект
    return JsonResponse({})


def simulate_heating_process(volume, initial_temp, target_temp, efficiency, power):
    T1 = initial_temp  # температура холодной воды в °C
    T2 = target_temp  # температура нагретой воды в °C
    V = volume  # объем или масса воды в литрах (или кг)
    c = 4.187  # удельная теплоемкость воды в кДж/(кг·°C)

    # Рассчитываем расход электроэнергии в кВт·ч, учитывая КПД
    energy_kWh = (3600 * (T2 - T1) * V * c) / (efficiency/100 * 3600)

    # Рассчитываем время в часах, необходимое для нагрева
    time_hours = energy_kWh / power

    return energy_kWh, time_hours
