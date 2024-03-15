from django.contrib import admin
from office import models
# Register your models here.
admin.site.register(models.Measurement)
admin.site.register(models.Place)
admin.site.register(models.Sensor)
admin.site.register(models.Cnc_machine)
admin.site.register(models.Cnc_model)
admin.site.register(models.Instrument)
admin.site.register(models.Material)
admin.site.register(models.Cnc_detail)
admin.site.register(models.Product)