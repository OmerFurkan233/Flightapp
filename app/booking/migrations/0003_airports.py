# Generated by Django 3.1.5 on 2021-01-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_flight_passenger'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('iata_code', models.CharField(blank=True, max_length=4, null=True)),
            ],
        ),
    ]