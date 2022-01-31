from django.shortcuts import render
from rest_framework import viewsets
from .models import CinemaHall, Movie, TicketRequest, Showing
from .serializers import CinemaHallSerializer, MovieSerializer, TicketRequestSerializer, ShowingSerializer

class CinemaHallView(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer

class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class TicketRequestView(viewsets.ModelViewSet):
    queryset = TicketRequest.objects.all()
    serializer_class = TicketRequestSerializer

class ShowingView(viewsets.ModelViewSet):
    queryset = Showing.objects.all()
    serializer_class = ShowingSerializer