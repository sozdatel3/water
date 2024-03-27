from email.policy import default
from os import name
from unittest.mock import DEFAULT
from django.db import models
# from django.utils import timezone
from django.utils import timezone
from django.core.serializers import serialize
from django.http import JsonResponse

class Place(models.Model):
    name = models.CharField(max_length = 256, primary_key = True)
    adress = models.CharField(max_length = 256)
    rent = models.DecimalField(max_digits = 9,decimal_places = 2,default = 0, null = False, help_text = 'Введите стоимость аренды')
    square = models.IntegerField(default = 0, null = False)
    
    def __str__(self):
        return self.name

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
    price = models.DecimalField(max_digits = 9,decimal_places = 2,default = 0, null = False , help_text = 'Введите стоимость инструмента')
    place_id = models.ForeignKey(Place, on_delete = models.PROTECT)
    qr = models.URLField( default = '-', null = False, help_text = 'Введите ссылку на QR код')
    purchase_date = models.DateField(default = timezone.now)
    
    def __str__(self):
        return self.name
#Functions block start
def add_instrument (name,purpose,shop,price,place,qr):
    Instrument.objects.create(name = name, purpose = purpose, shop = shop, price = price, place = place, qr = qr)
#Functions block end 
class Sensor(models.Model):
    name = models.CharField(max_length = 256)
    place_id = models.ForeignKey(Place, on_delete = models.PROTECT)
    purpose = models.TextField(null = False, help_text = 'Введите назначение датчика', default = '-')
    price = models.DecimalField(max_digits = 9,decimal_places = 2,default = 0, null = False , help_text = 'Введите стоимость датчика')
    shop_url = models.URLField(max_length = 256, default = 'Not Found', null = False, help_text = 'Введите ссылку на интернет-магазин')
    documentation = models.URLField(max_length = 256, default = 'Not Found', null = False, help_text = 'Введите ссылку на документацию')
    qr = models.URLField(max_length = 256, default = '-', null = False, help_text = 'Введите ссылку на QR-код')
    buy_date = models.DateField(default = timezone.now)
    
    def __str__(self):
        return self.name
#Functions block start
def add_sensor (name, purpose, price, shop_url, documentation, qr):
    #Функция добавляет данные в таблицу Sensor(place нужно сделать выпадающим)
    Sensor.objects.create(name=name, purpose=purpose, price=price, shop_url=shop_url, documentation=documentation, qr=qr)
#Functions block end
class Product(models.Model):
    name = models.CharField(max_length = 256, help_text = 'Введите название товара', default = '-')
    place_id = models.ForeignKey(Place, on_delete = models.PROTECT)
    article = models.IntegerField(default = 0, null = False, help_text = 'Введите артикул товара')
    price = models.DecimalField(max_digits = 9,decimal_places = 2,default = 0, null = False , help_text = 'Введите стоимость товара')
    box_count = models.IntegerField(default = 0, null = False, help_text = 'Введите количество коробок')
    item_count = models.IntegerField(default = 0, null = False, help_text = 'Введите количество товара в коробке')
    box_size = models.FloatField(default = 0, null = False, help_text = 'Введите объем коробки')
    item_size = models.FloatField(default = 0, null = False, help_text = 'Введите объем товара')
    image = models.ImageField(upload_to='item_images')
    qr = models.URLField(max_length = 256, default = '-', null = False, help_text = 'Введите ссылку на QR-код')
    buy_date = models.DateField(default = timezone.now)
    
    def __str__(self):
        return f'Наименование: {self.name}| Артикул: {self.article}'
    
#Functions block start
def add_product(name, article, box_count, item_count, box_size, item_size, qr):
#Функция добавляет данные в таблицу Product(place нужно сделать выпадающим)
    Product.objects.create(name = name, article = article, box_count = box_count, item_count = item_count, box_size = box_size, item_size = item_size, qr = qr)

#Functions block end
class Cnc_machine(models.Model):
    name = models.CharField(max_length = 256, help_text = 'Введите название чпу', default = '-')
    place_id = models.ForeignKey(Place, on_delete = models.PROTECT)
    purpose = models.CharField(max_length = 256, default = '-', null = False, help_text = 'Введите назначение чпу')
    price = models.DecimalField(max_digits = 9,decimal_places = 2,default = 0, null = False , help_text = 'Введите стоимость чпу станка')
    documentation = models.URLField(max_length = 256, default = '-', null = False, help_text = 'Введите ссылку на документацию чпу')
    qr = models.URLField(max_length = 256, default = '-', null = False, help_text = 'Введите ссылку на QR-код чпу')
    buy_date = models.DateField(default = timezone.now)
    
    def __str__(self):
        return self.name
#Functions block start
def add_cnc_machine(name, purpose, price, documentation, qr):
#Функция добавляет данные в таблицу Cnc_machine(place нужно сделать выпадающим)
    Cnc_machine.objects.create(name = name, purpose = purpose, price = price, documentation = documentation, qr = qr)
#Functions block end
class Material(models.Model):
    name = models.CharField(max_length = 256, help_text = 'Введите название материала', default = '-')
    place_id = models.ForeignKey(Place, on_delete = models.PROTECT)
    color = models.CharField(max_length = 256, default = '-', null = False, help_text = 'Введите цвет материала')
    weight = models.FloatField(default = 0, null = False, help_text = 'Введите вес материала')
    amount = models.FloatField(default = 0, null = False, help_text = 'Введите количество материала')
    structure = models.CharField(max_length = 256, default = '-', null = False, help_text = 'Введите структуру материала')
    cost = models.DecimalField(max_digits = 9,decimal_places = 2,default = 0, null = False , help_text = 'Введите стоимость материала')
    buy_date = models.DateField(default = timezone.now)
    
    
    def __str__(self):
        return self.name
#Functions block start
def add_material(name, color, weight, amount, structure, cost):
#Функция добавляет данные в таблицу Material(place нужно сделать выпадающим)
    Material.objects.create(name = name, color = color, weight = weight, amount = amount, structure = structure, cost = cost)

#Functions block end
class Cnc_detail(models.Model):
    name = models.CharField(max_length = 256, help_text = 'Введите название детали', default = '-')
    place_id = models.ForeignKey(Place, on_delete = models.PROTECT)
    weight = models.FloatField(default = 0, null = False, help_text = 'Введите вес детали') 
    purpose = models.CharField(max_length = 256, default = '-', null = False, help_text = 'Введите назначение детали')
    documentation = models.URLField(max_length = 256, default = '-', null = False, help_text = 'Введите ссылку на документацию детали')  
    qr = models.URLField(max_length = 256, default = '-', null = False, help_text = 'Введите ссылку на QR детали')
    
    
    def __str__(self):
        return self.name
#Functions block start
def add_cnc_detail(name, weight, purpose, documentation, qr):
#Функция добавляет данные в таблицу Cnc_detail(place нужно сделать выпадающим)
    Cnc_detail.objects.create(name = name, weight = weight, purpose = purpose, documentation = documentation, qr = qr)

#Functions block end 
class Cnc_model(models.Model):
    name = models.CharField(max_length = 256, help_text = 'Введите название модели', default = '-')
    machine_id = models.ForeignKey(Cnc_machine, on_delete = models.PROTECT)
    place_id = models.ForeignKey(Place, on_delete = models.PROTECT)
    weight = models.FloatField(default = 0, null = False, help_text = 'Введите вес модели')
    material_id = models.ForeignKey(Material, on_delete = models.PROTECT)
    cost = models.DecimalField(max_digits = 9,decimal_places = 2,default = 0, null = False , help_text = 'Введите стоимость модели')
    amount_material = models.IntegerField(default = 0, null = False, help_text = 'Введите количество материала')
    production_time = models.FloatField(default = 0, null = False, help_text = 'Введите время производства')
    production_date = models.DateField(default = timezone.now)
    cnc_detail_id = models.ForeignKey(Cnc_detail, on_delete = models.PROTECT)
    cnc_detail_documentation = models.URLField(max_length = 256, default = '-', help_text = 'Введите ссылку на документацию модели')
    qr = models.URLField(max_length = 256, default = '-', help_text = 'Введите ссылку на QR код модели')
    
    
    def __str__(self):
        return self.name
#Functions block start
def add_cnc_model(name, machine_id, weight, material_id, cost, amount_material, production_time, cnc_detail_id, cnc_detail_documentation, qr):
    Cnc_model.objects.create(name = name, machine_id = machine_id, weight = weight, material_id = material_id, cost = cost, amount_material = amount_material, production_time = production_time, cnc_detail_id = cnc_detail_id, cnc_detail_documentation = cnc_detail_documentation, qr = qr)
#Функция добавляет данные в таблицу Cnc_model(place нужно сделать выпадающим)

#Functions blok end