from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Event , Location
from .serializers import EventSerializer, LocationSerializer
from rest_framework.decorators import api_view
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'Pages/index.html')#tamplates yolu kayitli oldğu için
                                            #sadece pages/index kullanarak
                                            #istenilen dosyaya erişebiliyoruz
def about(request):
    return render(request, 'Pages/about.html')


def events(request):
    all_event_data = {}

    all_event_data['dataset'] = Event.objects.all()
    
    return render(request, 'Pages/events.html' ,all_event_data)


def event_details(request,id):
    event_data = {}
    
    event_data = Event.objects.get(pk=id)
    
    return render(request, 'Pages/event_detail.html', {'dataset' : event_data})

@api_view(['GET','POST'])
def create_event(request):
    if request.method == 'POST':
        event_name = request.POST['event_name']
        description = request.POST['description']
        event_date = request.POST['event_date']
        event_time = request.POST['event_time']
        location_id =request.POST['location_id']
        
        if Event.objects.filter(event_name = event_name).first():
            messages.add_message(request, messages.WARNING, "Event name is taken")
            return redirect('create_event')
        else:
            
            Event.objects.create(event_name= event_name, description= description,
                event_date= event_date, event_time=event_time, location_id= location_id)  
            messages.add_message(request, messages.SUCCESS, "Event created")
            return redirect('events')
    else:
        locations = Location.objects.all()
        
        print(locations)
        
        return render(request, 'Pages/create_event.html', {'locations' : locations})   
    
@api_view(['GET','POST'])
def create_location(request): 
    if request.method == 'POST':
        location_name = request.POST['location_name']
        
        
        if Location.objects.filter(location_name = location_name).first():
            messages.add_message(request, messages.WARNING, "Location exists")
            return redirect('create_location')
        else:
            
            Location.objects.create(location_name= location_name)  
            messages.add_message(request, messages.SUCCESS, "Location created")  
            return redirect('create_event')
    else:
        return render(request, 'Pages/create_location.html')
        


def api_events(request):
    events = Event.objects.all()
    
    serializer = EventSerializer(events, many=True)
    
    return JsonResponse(serializer.data, safe=False)


def api_events_single(request,id):
    events = Event.objects.get(pk=id)
    
    serializer = EventSerializer(events, many=False)
    
    return JsonResponse(serializer.data, safe=False)


def api_locations(request):
    location = Location.objects.all()
    
    serializer = LocationSerializer(location, many=True)
    
    return JsonResponse(serializer.data, safe=False)


def api_locations_single(request,id):
    location = Location.objects.get(pk=id)
    
    serializer = LocationSerializer(location, many=False)
    
    return JsonResponse(serializer.data, safe=False)