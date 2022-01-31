from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cinemaHalls', views.CinemaHallView)
router.register('movies', views.MovieView)
router.register('ticketRequests', views.TicketRequestView)
router.register('showings', views.ShowingView)

urlpatterns = [
    path('', include(router.urls))
]