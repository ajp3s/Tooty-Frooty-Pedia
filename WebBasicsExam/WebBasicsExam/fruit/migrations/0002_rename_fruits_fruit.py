# Generated by Django 4.2.2 on 2023-06-24 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fruits',
            new_name='Fruit',
        ),
    ]