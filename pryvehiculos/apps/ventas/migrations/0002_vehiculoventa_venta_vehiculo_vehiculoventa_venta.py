# Generated by Django 4.0.4 on 2022-05-20 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0002_rename_tipovehiculo_vehiculo_tipovehiculo'),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehiculoVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.BigIntegerField()),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.vehiculo')),
            ],
        ),
        migrations.AddField(
            model_name='venta',
            name='vehiculo',
            field=models.ManyToManyField(through='ventas.VehiculoVenta', to='vehiculos.vehiculo'),
        ),
        migrations.AddField(
            model_name='vehiculoventa',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.venta'),
        ),
    ]
