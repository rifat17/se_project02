# Generated by Django 3.0.1 on 2020-01-25 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='roomType',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='room.RoomType'),
            preserve_default=False,
        ),
    ]