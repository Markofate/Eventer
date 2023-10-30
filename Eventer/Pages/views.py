from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Event , Location
from .serializers import EventSerializer, LocationSerializer

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
    
    event_data['dataset'] = Event.objects.get(pk=id)
    
    return render(request, 'Pages/event_detail.html', event_data)


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