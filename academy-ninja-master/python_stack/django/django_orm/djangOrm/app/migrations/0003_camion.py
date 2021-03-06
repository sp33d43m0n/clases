# Generated by Django 4.0.2 on 2022-02-20 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_ciudad_cantidad_habitantes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('C2', 'DOS EJES'), ('C4', 'CUATRO EJES'), ('C6', 'SEIS EJES')], default='C2', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
