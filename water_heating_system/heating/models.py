from django.db import models


class Container(models.Model):
    volume = models.FloatField("Объем л или кг")
    initial_temperature = models.FloatField("Начальная температура °C")
    target_temperature = models.FloatField("Конечная температура °C")
    efficiency = models.FloatField("КПД %", default=100)
    # power = models.FloatField("Мощность (кВт)", default=100)
