# Generated by Django 5.0.3 on 2024-03-23 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_rename_bio_person_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='mensage',
            new_name='bio',
        ),
    ]
