# Generated by Django 4.2.2 on 2023-06-24 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0003_fruit_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fruit',
            name='user',
        ),
    ]
