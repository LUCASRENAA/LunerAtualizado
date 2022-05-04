# Generated by Django 3.0.7 on 2022-04-28 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_auto_20220424_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_arquivo', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='porta',
            name='dataAgora',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]