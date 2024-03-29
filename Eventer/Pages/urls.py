from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('events', views.events, name='events'),
    path('events/<int:id>', views.event_details, name='event_details'),
    path('api/events', views.api_events, name='api_events'),
    path('api/location', views.api_locations, name='api_locations'),
    path('api/events/<int:id>', views.api_events, name='api_events_single'),
    path('create-event', views.create_event, name='create_event'),
    path('create-location', views.create_location, name='create_location'),
    path('events/delete-event/<int:id>', views.event_delete,name='event_delete'),
]
