from rest_framework import serializers
from .models import CinemaHall, Movie, TicketRequest, Showing

class CinemaHallSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ('id', 'url', 'name', 'rows', 'columns')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ShowingSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=True)
    cinemaHall = CinemaHallSerializer(many=True)
    
    class Meta:
        model = Showing
        fields = ('id', 'url', 'movie', 'date', 'cinemaHall', 'isTicketAvailable')

class TicketRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TicketRequest
        fields = ('id', 'url', 'showingId', 'rowId', 'columnId')


# class CinemaHallSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CinemaHall
#         fields = '__all__'

# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = '__all__'

# class ShowingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Showing
#         fields = '__all__'

# class TicketRequestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TicketRequest
#         fields = '__all__'