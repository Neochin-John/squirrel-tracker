from django.urls import path

from . import views

app_name='squirrel'

urlpatterns=[
        path('map/',views.map_view),
        path('sightings/',views.list_all_sightings),
        path('sightings/add/',views.create_sighting,name='create_sighting'),
        path('sightings/stats/',views.general_stats),
        
        path('sightings/<unique_squirrel_id>/',views.update_sighting,name='update_sighting'),
]
