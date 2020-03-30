# Generated by Django 3.0.1 on 2020-01-27 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotelroom', '0002_auto_20200127_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelroom',
            name='rProperty',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hotelroom.Property'),
        ),
        migrations.AlterField(
            model_name='roombooking',
            name='bProperty',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hotelroom.Payment'),
        ),
        migrations.AlterField(
            model_name='roombooking',
            name='bRoom',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hotelroom.HotelRoom'),
        ),
    ]
