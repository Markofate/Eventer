from django.shortcuts import render
from django.http import HttpResponse
from .models import Event , Location 

# Create your views here.


def index(request):
    return render(request, 'Pages/index.html')#tamplates yolu kayitli oldğu için
                                            #sadece pages/index kullanarak
                                            #istenilen dosyaya erişebiliyoruz
def about(request):
    return render(request, 'Pages/about.html')


def events(request,id=None):
    all_event_data = {}

    all_event_data['dataset'] = Event.objects.all()
    
    return render(request, 'Pages/events.html' ,all_event_data)


def event_details(request,id):
    event_data = {}
    
    event_data['dataset'] = Event.objects.get(pk=id)
    
    return render(request, 'Pages/event_detail.html', event_data)

