from django.shortcuts import render

from .models import Sighting

def map_view(request):
    context={}
    return render(request,'squirrel/map.html',context)

def list_all_sightings(request):
    return render(request,'squirrel/map.html',{})

def update_sighting(request):
    return render(request,'squirrel/map.html',{})

def create_sighting(request):
    return render(request,'squirrel/map.html',{})

def general_stats(request):
    return render(request,'squirrel/map.html',{})
    
# Create your views here.
