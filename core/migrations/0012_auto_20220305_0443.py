# Generated by Django 3.0.7 on 2022-03-05 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_pentest_rede_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='comando',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='scan',
            name='dataAgora',
            field=models.CharField(max_length=50),
        ),
    ]
