# Generated by Django 2.1 on 2018-09-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='kucun',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='maichu',
            field=models.IntegerField(default=0),
        ),
    ]
