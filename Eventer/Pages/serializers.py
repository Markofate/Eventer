from rest_framework import serializers
from Pages.models import Location , Event


class LocationSerializer(serializers.ModelSerializer):
    class Meta :
        model = Location
        fields = ('location_id','location_name')


class EventSerializer(serializers.ModelSerializer):
    class Meta :
        model = Event
        fields = ('event_id','event_name', 'description','event_date','event_time','location')



