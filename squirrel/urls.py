from django.urls import path

from . import views

urlpatterns=[
        path('map/',views.map_view),
        path('sightings/',views.list_all_sightings),
        path('sightings/<unique-squirrel-id>/',views.update_sighting),
        path('sightings/add/',views.create_sighting),
        path('sightings/stats/',views.general_stats),
]
