# Generated by Django 4.1.2 on 2024-06-12 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_entrada'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entrada',
            new_name='Ticket',
        ),
    ]
