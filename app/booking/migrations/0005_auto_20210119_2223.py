# Generated by Django 3.1.5 on 2021-01-19 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20210119_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrHour',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='deptHour',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='duration',
            field=models.CharField(max_length=100, null=True),
        ),
    ]