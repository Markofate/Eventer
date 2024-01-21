from django.contrib import admin

# Register your models here.

from .models import Location, Event


# Register the Location model
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_name', )

# Register the Event model
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_date', 'event_time', 'location', 'event_img')
    list_filter = ('event_date', 'location')
    search_fields = ('event_name', 'location__location_name')  # You can search by location name
    date_hierarchy = 'event_date'
    list_per_page = 15

# Register the User model
