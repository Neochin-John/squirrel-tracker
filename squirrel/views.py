from django.shortcuts import render

from .models import Sighting

from django.shortcuts import get_object_or_404

def map_view(request):
    context={}
    return render(request,'squirrel/map.html',context)

def list_all_sightings(request):
    sightings=Sighting.objects.all()
    context={
            'sightings':sightings                            # To be revised
    }
    return render(request,'squirrel/list_all_sightings.html',context)

def update_sighting(request,unique_squirrel_id):
    sighting=get_object_or_404(Sighting,pk=unique_squirrel_id)
    context={
            'sighting':sighting
    }
    return render(request,'squirrel/update_sighting.html',context)

def create_sighting(request):
    return render(request,'squirrel/map.html',{})

def general_stats(request):
    return render(request,'squirrel/map.html',{})
    
# Create your views here.
