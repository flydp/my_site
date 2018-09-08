# Generated by Django 2.1 on 2018-09-06 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=19.99, max_digits=6),
            preserve_default=False,
        ),
    ]
