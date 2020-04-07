# Generated by Django 3.0.3 on 2020-03-31 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_auto_20200330_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passengers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=40)),
                ('last', models.CharField(max_length=40)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flight.Flights')),
            ],
        ),
    ]
