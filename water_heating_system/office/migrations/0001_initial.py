# Generated by Django 3.2.23 on 2024-02-28 17:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='measurements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('rate', models.FloatField()),
                ('measurement_unit', models.CharField(max_length=20)),
                ('measurement_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]