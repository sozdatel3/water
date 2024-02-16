from django.db import models


class Container(models.Model):
    volume = models.FloatField("Объем л или кг")
    initial_temperature = models.FloatField("Начальная температура °C")
    target_temperature = models.FloatField("Конечная температура °C")
    efficiency = models.FloatField("КПД %", default=100)
    # power = models.FloatField("Мощность (кВт)", default=100)


class Room(models.Model):
    length = models.FloatField(default=2.0)  # Длина в метрах
    width = models.FloatField(default=1.0)  # Ширина в метрах
    wall_thickness = models.FloatField(default=0.1)  # Толщина стен в метрах
    temperature_udel = models.FloatField(default=0.028)  # Теплопроводность
    temperature = models.FloatField()  # Температура в помещении
