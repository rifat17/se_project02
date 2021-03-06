# Generated by Django 3.0.1 on 2020-01-27 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelroom', '0005_auto_20200127_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hotelroom',
            name='rdiscount',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='hotelroom',
            name='rprice',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]
