# Generated by Django 3.2.9 on 2022-01-30 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CinemaHall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rows', models.PositiveIntegerField()),
                ('columns', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=50)),
                ('duration', models.PositiveIntegerField()),
                ('releaseDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TicketRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showingId', models.PositiveIntegerField()),
                ('rowId', models.PositiveIntegerField()),
                ('columnId', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Showing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('isTicketAvailable', models.BooleanField()),
                ('cinemaHall', models.ManyToManyField(to='cinemas.CinemaHall')),
                ('movie', models.ManyToManyField(to='cinemas.Movie')),
            ],
        ),
    ]