# Generated by Django 4.2.2 on 2023-06-29 14:24

import WebBasicsExam.profiles.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, validators=[WebBasicsExam.profiles.models.start_with_letter_validator, django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(max_length=35, validators=[WebBasicsExam.profiles.models.start_with_letter_validator, django.core.validators.MinLengthValidator(1)])),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(8)])),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='Image URL')),
                ('age', models.IntegerField(blank=True, default=18, null=True)),
            ],
        ),
    ]
