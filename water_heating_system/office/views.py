from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


def office_main_view(request):
    return render(request, 'office/html/main.html')


@csrf_exempt  #TODO Убрать в проде
@require_http_methods(["POST"])
def handle_weather_data(request):
    # Сохраняем данные из POST-запроса в сессии
    request.session['temperature'] = request.POST.get('temperature')
    request.session['humidity'] = request.POST.get('humidity')
    return JsonResponse({"status": "Received", "temperature": request.session['temperature'], "humidity": request.session['humidity']})

def office_main_view(request):
    # При AJAX-запросе возвращаем данные в JSON
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        temperature = request.session.get('temperature', '--')
        humidity = request.session.get('humidity', '--')
        return JsonResponse({"temperature": temperature, "humidity": humidity})
    # Для обычного запроса рендерим HTML-шаблон
    return render(request, 'office/main.html')