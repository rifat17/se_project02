# Generated by Django 3.0.1 on 2020-01-25 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('max_capacity', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('CONFIRMED', 'Confirmed'), ('CANCLE', 'Cancle'), ('NONE', 'None')], default='NONE', max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotel.Hotel')),
            ],
        ),
    ]
