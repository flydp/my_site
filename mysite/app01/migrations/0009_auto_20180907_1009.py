# Generated by Django 2.1 on 2018-09-07 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_auto_20180906_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=9.9, max_digits=6),
        ),
    ]