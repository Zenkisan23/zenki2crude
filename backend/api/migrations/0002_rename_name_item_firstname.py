# Generated by Django 5.0.6 on 2024-07-05 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='Firstname',
        ),
    ]
