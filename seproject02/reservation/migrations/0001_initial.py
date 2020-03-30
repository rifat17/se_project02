# Generated by Django 3.0.1 on 2020-01-25 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_in', models.DateField()),
                ('date_out', models.DateField()),
                ('made_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReservedRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_rooms', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('reservation_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='reservation.Reservation')),
                ('roomType_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='room.RoomType')),
            ],
        ),
        migrations.CreateModel(
            name='OccupiedRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('reservation_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='reservation.Reservation')),
                ('room_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='room.Room')),
            ],
        ),
    ]