# Generated by Django 3.0.1 on 2020-01-28 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotelroom', '0006_auto_20200127_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('rating_count', models.IntegerField()),
                ('rated_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hotelroom.HotelRoom')),
            ],
        ),
    ]