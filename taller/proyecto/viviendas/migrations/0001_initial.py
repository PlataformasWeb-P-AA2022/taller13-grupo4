# Generated by Django 4.0.5 on 2022-07-13 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30, unique=True)),
                ('tipo', models.CharField(choices=[('residencial', 'Residencial'), ('comercial', 'Comercial')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_propietario', models.CharField(max_length=100)),
                ('costo_departamento', models.IntegerField(verbose_name='costo departamento')),
                ('num_cuartos', models.IntegerField(verbose_name='numero de cuartos')),
                ('edificio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamentos', to='viviendas.edificio')),
            ],
        ),
    ]