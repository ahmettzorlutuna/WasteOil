# Generated by Django 4.0.1 on 2022-01-17 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oil', '0002_oil_price_alter_oil_liter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oil',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
