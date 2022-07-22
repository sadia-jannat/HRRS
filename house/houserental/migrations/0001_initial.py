# Generated by Django 3.1.5 on 2022-07-15 02:43

from django.db import migrations, models
import houserental.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ownerformfill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownername', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phn', models.IntegerField()),
                ('housecategory', models.CharField(choices=[('flat', 'flat'), ('duplex', 'duplex'), ('commercial', ' commercial'), ('family_house', 'family_house')], max_length=200)),
                ('housename', models.CharField(max_length=100)),
                ('houserent', models.PositiveIntegerField(default=0)),
                ('img', models.ImageField(blank=True, null=True, upload_to=houserental.models.fileimg)),
                ('imgidfont', models.ImageField(blank=True, null=True, upload_to=houserental.models.fileimg)),
                ('imgidback', models.ImageField(blank=True, null=True, upload_to=houserental.models.fileimg)),
                ('division', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=100)),
                ('area', models.CharField(blank=True, max_length=250, verbose_name='Area')),
                ('housesize', models.IntegerField()),
                ('bedroom', models.PositiveIntegerField(default=0)),
                ('dinning', models.PositiveIntegerField(default=0)),
                ('drawing', models.PositiveIntegerField(default=0)),
                ('bathroom', models.PositiveIntegerField(default=0)),
                ('kitchen', models.PositiveIntegerField(default=0)),
                ('balcony', models.PositiveIntegerField(default=0)),
                ('allinfo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Ownerformfill',
                'verbose_name_plural': 'Ownerformfill',
            },
        ),
    ]
