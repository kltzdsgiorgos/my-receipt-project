# Generated by Django 4.1 on 2022-09-09 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fill_date', models.DateTimeField(verbose_name='date filled')),
                ('fuel_type', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=20)),
                ('gas_station', models.CharField(max_length=10)),
                ('price_per_liter', models.FloatField()),
                ('liters', models.FloatField()),
                ('gas_total_price', models.FloatField()),
            ],
        ),
    ]
