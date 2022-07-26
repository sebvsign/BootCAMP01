# Generated by Django 4.0.5 on 2022-07-22 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('rutCliente', models.IntegerField(primary_key=True, serialize=False, verbose_name='rut_cliente')),
                ('nombreCliente', models.CharField(max_length=50, verbose_name='Nombre del Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('idSucursal', models.IntegerField(primary_key=True, serialize=False, verbose_name='sucursal id: ')),
                ('region', models.CharField(max_length=100, verbose_name='region')),
                ('comuna', models.CharField(max_length=100, verbose_name='comuna')),
                ('direccion', models.CharField(max_length=100, verbose_name='direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('idVehiculo', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id del vehiculo')),
                ('patente', models.CharField(max_length=6, verbose_name='Patente')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca vehiculo')),
                ('modelo', models.CharField(blank=True, max_length=20, null=True, verbose_name='Modelo')),
                ('color', models.CharField(max_length=20, verbose_name='Color vehiculo')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='Vendedores',
            fields=[
                ('rutVendedor', models.IntegerField(primary_key=True, serialize=False, verbose_name='rut_vededor')),
                ('nombreVendedor', models.CharField(max_length=50, verbose_name='Nombre del vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('idVenta', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id venta')),
                ('cantidadVenta', models.IntegerField(blank=True, null=True)),
                ('Vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vehiculo')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.clientes')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vendedores')),
            ],
        ),
    ]
