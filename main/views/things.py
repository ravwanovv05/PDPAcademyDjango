from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from main.models import Thing
from main.serializers.things import ThingSerializer


class ThingsListView(GenericAPIView):
    serializer_class = ThingSerializer

    def get_queryset(self):
        return Thing.objects.all()

    def get(self, request, *args, **kwargs):
        things = Thing.objects.all()
        serializer = self.get_serializer(things, many=True)

        return Response(serializer.data)

