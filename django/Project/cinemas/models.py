from tkinter import CASCADE
from django.db import models

class CinemaHall(models.Model):
    name = models.CharField(max_length=50)
    rows = models.PositiveIntegerField()
    columns = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()
    releaseDate = models.DateTimeField()

    def __str__(self):
        return self.title

class Showing(models.Model):
    movie = models.ManyToManyField(Movie)
    date = models.DateTimeField()
    cinemaHall = models.ManyToManyField(CinemaHall)
    isTicketAvailable = models.BooleanField()

    def __str__(self):
        return str(self.id)

class TicketRequest(models.Model):
    showingId = models.PositiveIntegerField()
    rowId = models.PositiveIntegerField()
    columnId = models.PositiveIntegerField()

    def __str__(self):
        return str(self.showingId)