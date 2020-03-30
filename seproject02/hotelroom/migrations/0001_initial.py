# Generated by Django 3.0.1 on 2020-01-27 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rcode', models.CharField(blank=True, max_length=10)),
                ('rname', models.CharField(blank=True, max_length=30)),
                ('rphoto', models.ImageField(default='room.jpg', upload_to='room/')),
                ('rprice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rdiscount', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('ONLINE', 'Oneline'), ('HAND', 'Hand')], default='ONLINE', max_length=10)),
                ('date', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sqfeet', models.CharField(max_length=20)),
                ('no_of_bed', models.IntegerField()),
                ('no_of_bathroom', models.IntegerField()),
                ('food', models.BooleanField(default=False)),
                ('rules', models.TextField()),
                ('capacity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='RoomBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bChecked_in', models.BooleanField(default=False)),
                ('bChecked_out', models.BooleanField(default=False)),
                ('bChecked_in_date', models.DateField()),
                ('bChecked_out_date', models.DateField()),
                ('bProperty', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotelroom.Payment')),
                ('bRoom', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotelroom.HotelRoom')),
            ],
        ),
        migrations.AddField(
            model_name='hotelroom',
            name='rProperty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotelroom.Property'),
        ),
        migrations.AddField(
            model_name='hotelroom',
            name='rhotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotel.Hotel'),
        ),
    ]