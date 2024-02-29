from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import get_last_measurement, add_measurement, get_all_measurement_json


# def office_main_view(request):
#     return render(request, 'office/html/main.html')


# @csrf_exempt  #TODO Убрать в проде
# @require_http_methods(["POST"])
# def handle_weather_data(request):
#     # Сохраняем данные из POST-запроса в сессии
#     request.session['temperature'] = request.POST.get('temperature')
#     request.session['humidity'] = request.POST.get('humidity')
#     return JsonResponse({"status": "Received", "temperature": request.session['temperature'], "humidity": request.session['humidity']})

def office_main_view(request):
    # При AJAX-запросе возвращаем данные в JSON
    # if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # temperature = request.session.get('temperature', '--')
        # humidity = request.session.get('humidity', '--')
        # return JsonResponse({"temperature": temperature, "humidity": humidity})
    # Для обычного запроса рендерим HTML-шаблон
    return render(request, 'office/main.html')


@csrf_exempt
@require_http_methods(["POST"])
def set_temp(request):
    if request.method == 'POST':
        temperature = request.POST.get('temperature')
        humidity = request.POST.get('humidity')
        add_measurement("Temperature", temperature, "C")
        add_measurement("Humidity", humidity, "%")
        # OfficeData.objects.create(temperature=temperature, humidity=humidity)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

def get_latest_office_data(request):
    # data = OfficeData.objects.order_by('-updated_at').first()
    messurment_temp = get_last_measurement('Temperature')
    messurment_hum = get_last_measurement('Humidity')
    
    if messurment_temp and messurment_hum:
        return JsonResponse({'temperature': messurment_temp.rate, 'humidity': messurment_hum.rate})
    return JsonResponse({'error': 'No data available'}, status=404)

def get_measurements(request):
    if mesurements := get_all_measurement_json('Office'):
        print(mesurements)
        return JsonResponse(mesurements, safe=False)
    return JsonResponse({'error': 'No data available'}, status=404)
    