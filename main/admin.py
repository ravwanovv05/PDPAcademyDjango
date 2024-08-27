from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from main.models import Thing, Room
from main.resources import ThingResource, RoomResource


@admin.register(Room)
class RoomAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'room_number')
    list_display_links = ('id',)
    list_per_page = 10
    search_fields = ('name', 'room_number')
    resource_class = RoomResource


@admin.register(Thing)
class ThingAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    list_per_page = 10
    search_fields = ('id', 'name')
    resource_class = ThingResource

