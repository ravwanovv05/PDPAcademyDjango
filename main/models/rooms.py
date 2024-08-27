from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Name')
    room_number = models.IntegerField(verbose_name='Room number')

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return self.name
