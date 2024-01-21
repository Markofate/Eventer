from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Event , Location
from .serializers import EventSerializer, LocationSerializer
from rest_framework.decorators import api_view
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json
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

def event_delete(request,id):

    event = Event.objects.get(pk= id)
    event = Event.delete(self=event)
        
    return redirect('events')
    
@api_view(['GET','POST'])
def create_event(request):
    if request.method == 'POST':
        event_name = request.POST['event_name']
        description = request.POST['description']
        event_date = request.POST['event_date']
        event_time = request.POST['event_time']
        location_id = request.POST['location_id']
        event_img = request.FILES['event_img']
        creator =  request.user
        
        
        if Event.objects.filter(event_name = event_name).first():
            messages.add_message(request, messages.WARNING, "Event name is taken")
            return redirect('create_event')
        else:
                Event.objects.create(event_name=event_name, description=description,
                event_date=event_date,event_time=event_time,location_id=location_id,
                event_img=event_img, creator=creator)
                messages.add_message(request, messages.SUCCESS, "Event created")
                return redirect('events')
    else:
        locations = Location.objects.all()
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
        

@api_view(['GET','POST','PUT','DELETE'])
def api_events(request, id=None):
    
    if request.method == 'GET' and id is not None:
        events = Event.objects.get(pk= id) #single event get
    
        serializer = EventSerializer(events)
    
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'GET':
        events = Event.objects.all()
    
        serializer = EventSerializer(events, many=True)
    
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        
        event_id = request.data.get('event_id')
        event_name = request.data.get('event_name')
        description = request.data.get('description')
        event_date = request.data.get('event_date')
        event_time = request.data.get('event_time')
        location = request.data.get('location')
        
        Event.objects.create(event_id= event_id, event_name= event_name,
        description= description, event_date= event_date,event_time= event_time,
        location_id= location)
        
        return JsonResponse(request.data, safe=False)
    elif request.method == 'PUT':
        
        event = Event.objects.get(pk= id)
        
        data = json.loads(request.body)
       
        event.event_id=data.get('event_id',event.event_id)
        event.event_name=data.get('event_name',event.event_name)
        event.description=data.get('description',event.description)
        event.event_date=data.get('event_date',event.event_date)
        event.event_time=data.get('event_time',event.event_time)
            
        event.save()
        
        return JsonResponse(request.data, safe=False)
    
    
    elif request.method == 'DELETE':
        
        event = Event.objects.get(pk= id)
        event= Event.delete(self=event)
        
        return JsonResponse(request.data, safe=False)  
    
        
         
# def api_events_single(request,id):
#     if request.method == 'GET':
#         events = Event.objects.get(pk=id) tek bir tane çağırmak istiyorsak id ile çağrabiliriz
    
#         serializer = EventSerializer(events, many=False)
    
#         return JsonResponse(serializer.data, safe=False)

@api_view(['GET','POST'])
def api_locations(request):
    if request.method == 'GET':
        location = Location.objects.all()
    
        serializer = LocationSerializer(location, many=True)
    
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        
        location_id = request.data.get('location_id')
        location_name = request.data.get('location_name')
        
        Location.objects.create(location_id= location_id, location_name= location_name)
        
        return JsonResponse(request.data, safe=False)
        
