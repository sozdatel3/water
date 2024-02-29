from django.contrib import admin
from office import models
# Register your models here.
admin.site.register(models.measurement)
admin.site.register(models.Place)
admin.site.register(models.sensor)
admin.site.register(models.cnc_machine)
admin.site.register(models.cnc_model)
admin.site.register(models.instrument)
admin.site.register(models.material)