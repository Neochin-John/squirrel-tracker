from django.shortcuts import render

from .models import Sighting

from django.shortcuts import get_object_or_404

from .forms import SightingRequestForm

from django.http import JsonResponse

def map_view(request):
    sighthings = Sightings.objects.all()[:100]
    context={
            'sightings':sightings                            # To be revised
    }
    return render(request,'squirrel/map.html',context)

def list_all_sightings(request):
    sightings=Sighting.objects.all()
    context={
            'sightings':sightings                            # To be revised
    }
    return render(request,'squirrel/list_all_sightings.html',context)

def update_sighting(request,unique_squirrel_id):             #update the particular sight
    sighting=get_object_or_404(Sighting,pk=unique_squirrel_id)
    context={
            'sighting':sighting
    }
    return render(request,'squirrel/update_sighting.html',context)

def create_sighting(request):
    if request.method=='POST':
        form = SightingRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'errors':form.errors},status=400)

    return JsonResponse({})

def general_stats(request):
    sightings = Sighting.objects.all()

    total_number = sightings.count()
    count_black = sightings.filter(primary_fur_color='Black').count()
    count_running = sightings.filter(running='True').count()
    count_adult = sightings.filter(age='Adult').count()
    average_latitude = sightings.filter(latitude).average()

    context = {
            'total_number':total_number,
            'count_black':count_black,
            'count_running':count_running,
            'count_adult':count_adult,
            'average_latitude':average_latitude,
    }

    return render(request,'squirrel/stats.html',context)
    
# Create your views here.
