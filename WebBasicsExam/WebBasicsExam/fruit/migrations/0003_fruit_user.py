# Generated by Django 4.2.2 on 2023-06-24 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_profile'),
        ('fruit', '0002_rename_fruits_fruit'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruit',
            name='user',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
            preserve_default=False,
        ),
    ]
