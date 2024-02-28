
# Create your models here.
from django.db import models
from django.utils import timezone

class measurements(models.Model):                        
    name = models.CharField(max_length = 256)
    rate = models.FloatField()
    measurement_unit = models.CharField(max_length = 20)
    measurement_date = models.DateField(default = timezone.now)
#class places(models.Model):                              
    
def get_last_measurement (name):
    return measurements.objects.filter(name = name).order_by('id').last()

def add_measurement (name,rate,measurement_unit):
    measurements.objects.create(name = name, rate = rate, measurement_unit = measurement_unit)
