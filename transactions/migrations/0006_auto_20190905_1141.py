# Generated by Django 2.2.5 on 2019-09-05 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_auto_20190905_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='currency',
            field=models.FloatField(),
        ),
    ]