# Generated by Django 3.0.1 on 2020-01-27 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelroom', '0003_auto_20200127_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='method',
            field=models.CharField(choices=[('ONLINE', 'Online'), ('HAND', 'Hand')], default='ONLINE', max_length=10),
        ),
    ]
