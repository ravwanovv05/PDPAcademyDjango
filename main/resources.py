from import_export import resources
from main.models import Thing
from main.models import Room


class RoomResource(resources.ModelResource):
    class Meta:
        model = Room


class ThingResource(resources.ModelResource):
    class Meta:
        model = Thing
