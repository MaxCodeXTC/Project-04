# Generated by Django 2.2.5 on 2019-09-05 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_auto_20190904_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='reference',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.CharField(max_length=10),
        ),
    ]