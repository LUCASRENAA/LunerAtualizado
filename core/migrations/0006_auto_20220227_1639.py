# Generated by Django 3.0.7 on 2022-02-27 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_cve_cve_ip_porta_sistema_ip_sistemaoperacional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ffufcomandos',
            name='comando',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='ffufcomandos',
            name='dataAgora',
            field=models.CharField(max_length=31),
        ),
    ]
