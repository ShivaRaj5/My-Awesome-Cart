# Generated by Django 3.2.4 on 2021-08-22 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
