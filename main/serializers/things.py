from rest_framework import serializers
from main.models import Thing


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = '__all__'

