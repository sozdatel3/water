from django import forms
from .models import Container


class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = ['volume', 'initial_temperature',
                  'target_temperature', 'efficiency', 'power']
