# Generated by Django 4.1.2 on 2024-06-09 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='camisetas',
            fields=[
                ('codigo', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('detalle', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('oferta', models.BooleanField()),
                ('imagen', models.CharField(max_length=200)),
            ],
        ),
    ]
