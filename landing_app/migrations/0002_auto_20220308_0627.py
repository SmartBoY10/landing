# Generated by Django 3.0.4 on 2022-03-08 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workingtime',
            name='norm_hour',
            field=models.FloatField(default=8, verbose_name='Часы по нормативу'),
        ),
        migrations.AlterField(
            model_name='workingtime',
            name='hour',
            field=models.FloatField(verbose_name='Часы отработана'),
        ),
    ]
