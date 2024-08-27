from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from main.models import Room
from main.serializers.rooms import RoomSerializer


class RoomsListView(GenericAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.all()

    def get(self, request, *args, **kwargs):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)


