# Generated by Django 4.0.2 on 2022-04-03 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='Landlord',
            new_name='landlord',
        ),
    ]
