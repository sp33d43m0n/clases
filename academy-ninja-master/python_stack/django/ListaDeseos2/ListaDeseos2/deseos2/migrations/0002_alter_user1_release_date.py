# Generated by Django 3.2.9 on 2021-12-04 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deseos2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user1',
            name='release_date',
            field=models.DateField(),
        ),
    ]
