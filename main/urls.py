from django.urls import path
from main.views.rooms import RoomsListView
from main.views.things import ThingsListView

urlpatterns = [
    path('things-list', ThingsListView.as_view(), name='things_list'),
    path('rooms-list', RoomsListView.as_view(), name='rooms_list'),
]

