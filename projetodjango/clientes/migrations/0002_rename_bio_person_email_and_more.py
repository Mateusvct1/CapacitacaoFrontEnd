# Generated by Django 5.0.3 on 2024-03-22 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='bio',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='description',
            new_name='mensage',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='technologies_used',
        ),
        migrations.RemoveField(
            model_name='person',
            name='title',
        ),
    ]
