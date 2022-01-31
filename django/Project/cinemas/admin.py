from django.contrib import admin
from .models import CinemaHall, Movie, Showing, TicketRequest

admin.site.register(CinemaHall)
admin.site.register(Movie)
admin.site.register(Showing)
admin.site.register(TicketRequest)