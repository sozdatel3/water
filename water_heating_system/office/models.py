from email.policy import default
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
class Measurement(models.Model):
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
    return Measurement.objects.filter(name = name).order_by('id').last()

def add_measurement (name,rate,measurement_unit):
    '''Add new value for measurement table'''
    Measurement.objects.create(name = name, rate = rate, measurement_unit = measurement_unit)
    
def get_all_measurement_json(place_name):

    place_measurement = Measurement.objects.filter(place_id__name=place_name)
    return [
        {
            'name': m.name,
            'rate': m.rate,
            'measurement_date': str(m.measurement_date),
        }
        for m in place_measurement
    ]


class Instrument(models.Model):
    name = models.CharField(max_length = 256, help_text = 'Введите название инструмента', default = '-')
    purpose = models.TextField(null = False, help_text = 'Введите назначение инструмента', default = '-')
    shop = models.URLField( default = 'Not Found', null = False, help_text = 'Введите ссылку на инструмент')
    price = models.IntegerField(default = '0', null = False, help_text = 'Введите цену')
    place = models.ForeignKey(Place, on_delete = models.PROTECT, null = False)
    qr = models.URLField( default = '-', null = False, help_text = 'Введите ссылку на QR код')
    purchase_date = models.DateField(default = timezone.now)
#Functions block start
def add_instrument (name,purpose,shop,price,place,qr):
    Instrument.objects.create(name = name, purpose = purpose, shop = shop, price = price, place = place, qr = qr)
#Functions block end 
class Sensor(models.Model):
    name = models.CharField(max_length = 256)
    place = models.ForeignKey(Place, on_delete = models.PROTECT, null = False)
    purpose = models.TextField(null = False, help_text = 'Введите назначение датчика', default = '-')
    price = models.IntegerField(default = '0', null = False, help_text = 'Введите цену датчика')
    shop_url = models.URLField(max_length = 256, default = 'Not Found', null = False, help_text = 'Введите ссылку на интернет-магазин')
    documentation = models.URLField(max_length = 256, default = 'Not Found', null = False, help_text = 'Введите ссылку на документацию')
    qr = models.URLField(max_length = 256, default = '-', null = False, help_text = 'Введите ссылку на QR-код')
    buy_date = models.DateField(default = timezone.now)
#Functions block start
    
#Functions block end
class Product(models.Model):
    name = models.CharField(max_length = 256, help_text = 'Введите название товара', default = '-')
    place = models.ForeignKey(Place, on_delete = models.PROTECT, null = False)
    article = models.IntegerField(default = 0, null = False, help_text = 'Введите артикул товара')
    box_count = models.IntegerField(default = 0, null = False, help_text = 'Введите количество коробок')
    item_count = models.IntegerField(default = 0, null = False, help_text = 'Введите количество товара в коробке')
    box_size = models.IntegerField(default = 0, null = False, help_text = 'Введите объем коробки')
    item_size = models.IntegerField(default = 0, null = False, help_text = 'Введите объем товара')
    qr = models.URLField(max_length = 256, default = '-', null = False, help_text = 'Введите ссылку на QR-код')
    buy_date = models.DateField(default = timezone.now)
#Functions block start
    

#Functions block end
class Cnc_machine(models.Model):
    name = models.CharField(max_length = 256, help_text = 'Введите название чпу', default = '-')
    place = models.ForeignKey(Place, on_delete = models.PROTECT, null = False)
    purpose = models.CharField(max_length = 256, default = '-', null = False, help_text = 'Введите назначение чпу')
    price = models.IntegerField(default = 0, null = False, help_text = 'Введите цену чпу')
    documentation = models.URLField(max_length = 256, default = '-', null = False, help_text = 'Введите ссылку на документацию чпу')
    qr = models.URLField(max_length = 256, default = '-', null = False, help_text = 'Введите ссылку на QR-код чпу')
    buy_date = models.DateField(default = timezone.now)
#Functions block start
    

#Functions block end
class Material(models.Model):
    name = models.CharField(max_length = 256, help_text = 'Введите название материала', default = '-')
    place = models.ForeignKey(Place, on_delete = models.PROTECT, null = False)
    color = models.CharField(max_length = 256, default = '-', null = False, help_text = 'Введите цвет материала')
    weight = models.IntegerField(default = 0, null = False, help_text = 'Введите вес материала')
    amount = models.IntegerField(default = 0, null = False, help_text = 'Введите количество материала')
    structure = models.CharField(max_length = 256, default = '-', null = False, help_text = 'Введите структуру материала')
    cost = models.IntegerField(default = 0, null = False, help_text = 'Введите стоимость материала')
    buy_date = models.DateField(default = timezone.now)
#Functions block start



#Functions block end
class Cnc_detail(models.Model):
    name = models.CharField(max_length = 256, help_text = 'Введите название детали', default = '-')
    place = models.ForeignKey(Place, on_delete = models.PROTECT, null = False)
    weight = models.IntegerField(default = 0, null = False, help_text = 'Введите вес детали') 
    purpose = models.CharField(max_length = 256, default = '-', null = False, help_text = 'Введите назначение детали')
    documentation = models.URLField(max_length = 256, default = '-', null = False, help_text = 'Введите ссылку на документацию детали')  
    qr = models.URLField(max_length = 256, default = '-', null = False, help_text = 'Введите ссылку на QR детали')
#Functions block start



#Functions block end 
class Cnc_model(models.Model):
    name = models.IntegerField(max_length = 256, help_text = 'Введите название модели', default = '-')
    machine_id = models.ForeignKey(Cnc_machine, on_delete = models.PROTECT, null = False)
    place = models.ForeignKey(Place, on_delete = models.PROTECT, null = False)
    weight = models.IntegerField(default = 0, null = False, help_text = 'Введите вес модели')
    material_id = models.ForeignKey(Material, on_delete = models.PROTECT, null = False)
    cost = models.IntegerField(default = 0, null = False, help_text = 'Введите стоимость модели')
    amount_material = models.IntegerField(default = 0, null = False, help_text = 'Введите количество материала')
    production_time = models.IntegerField(default = 0, null = False, help_text = 'Введите время производства')
    production_date = models.DateField(default = timezone.now())
    cnc_detail_id = models.ForeignKey(Cnc_detail, on_delete = models.PROTECT, null = False)
    cnc_detail_documentation = models.URLField(max_length = 256, default = '-', help_text = 'Введите ссылку на документацию модели')
    qr = models.URLField(max_length = 256, default = '-', help_text = 'Введите ссылку на QR код модели')
#Functions block start
    

#Functions blok end