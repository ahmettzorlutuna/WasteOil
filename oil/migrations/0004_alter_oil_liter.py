# Generated by Django 4.0.1 on 2022-01-17 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oil', '0003_alter_oil_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oil',
            name='liter',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
