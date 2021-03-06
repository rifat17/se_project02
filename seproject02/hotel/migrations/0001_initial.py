# Generated by Django 3.0.1 on 2020-01-25 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=10)),
                ('name', models.CharField(blank=True, max_length=30)),
                ('motto', models.CharField(blank=True, max_length=30)),
                ('address', models.CharField(blank=True, max_length=30)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('state', models.CharField(blank=True, max_length=30)),
                ('zipCode', models.CharField(blank=True, max_length=10)),
                ('mobileNumber', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=30)),
                ('website', models.CharField(blank=True, max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('photo', models.ImageField(default='hotel.jpg', upload_to='hotel_pic')),
            ],
        ),
    ]
