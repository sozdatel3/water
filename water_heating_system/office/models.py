from os import name
from django.db import models
# from django.utils import timezone
from django.utils import timezone
from django.core.serializers import serialize
from django.http import JsonResponse
import json
class Place(models.Model):
    name = models.CharField(max_length = 256, primary_key = True)
    adress = models.CharField(max_length = 256)
    rent = models.IntegerField(default = 0, null = False)
    square = models.IntegerField(default = 0, null = False)

#Functions block start



#Functions block end
class measurement(models.Model):
    #Create table of measurement 
    name = models.CharField(max_length = 256)
    rate = models.FloatField()
    place_id = models.ForeignKey(Place, on_delete = models.PROTECT)
    measurement_unit = models.CharField(max_length = 20)
    measurement_date = models.DateField(default = timezone.now)
#TODO change function with place_id and changed all types off data
#Functions block
def get_last_measurement (name):
    '''Get last measurement'''
    return measurement.objects.filter(name = name).order_by('id').last()

def add_measurement (name,rate,measurement_unit):
    '''Add new value for measurement table'''
    measurement.objects.create(name = name, rate = rate, measurement_unit = measurement_unit)
    
def get_all_measurement_json(place_name):

    place_measurement = measurement.objects.filter(place_id__name=place_name)
    return [
        {
            'name': m.name,
            'rate': m.rate,
            'measurement_date': str(m.measurement_date),
        }
        for m in place_measurement
    ]


class sensor(models.Model):
    name = models.CharField(max_length = 256)
    place_id = models.IntegerField()
    purpose = models.TextField(null = False, help_text = 'Введите назначение датчика', default = '-')
    price = models.IntegerField(default = '0', null = False, )
    shop_url = models.URLField(max_length = 256, default = 'Not Found', null = False)
    documentation = models.URLField(max_length = 256, default = 'Not Found', null = False)
    qr = models.URLField(max_length = 256, default = '-', null = False)
    buy_date = models.IntegerField()
#Functions block start
    
#Functions block end
class cnc_machine(models.Model):
    model_name = models.IntegerField()
    place_id = models.IntegerField()
    purpose = models.IntegerField()
    price = models.IntegerField()
    documentation = models.IntegerField()
    qr = models.IntegerField()
    buy_date = models.IntegerField()
#Functions block start
    

#Functions block end
class cnc_model(models.Model):
    name = models.IntegerField()
    machine_id = models.IntegerField()
    place_id = models.IntegerField()
    weight = models.IntegerField()
    material_id = models.IntegerField()
    cost = models.IntegerField()
    amount_material = models.IntegerField()
    production_time = models.IntegerField()
    production_date = models.IntegerField()
    cnc_detail_id = models.IntegerField()
    cnc_detail_documentation = models.IntegerField()
    qr = models.IntegerField()
#Functions block start
    

#Functions blok end
class instrument(models.Model):
    name = models.IntegerField()
    purpose = models.IntegerField()
    place_id = models.IntegerField()
    shop = models.IntegerField()
    buy_date = models.IntegerField()
    price = models.IntegerField()
    qr = models.IntegerField()
#Functions block start 
    

#Functions block end
class material(models.Model):
    name = models.IntegerField()
    place_id = models.IntegerField()
    color = models.IntegerField()
    weight = models.IntegerField()
    amount = models.IntegerField()
    structure = models.IntegerField()
    cost = models.IntegerField()
    buy_date = models.IntegerField()
#Functions block start



#Functions block end
class cnc_detail(models.Model):
    name = models.IntegerField()
    place_id = models.IntegerField()
    weight = models.IntegerField() 
    purpose = models.IntegerField()
    documentation = models.IntegerField()   