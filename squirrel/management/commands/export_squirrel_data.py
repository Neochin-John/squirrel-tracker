from django.core.management.base import BaseCommand
from project.models import Squirrels
import csv

class Command(BaseCommand):
    help = 'Export all data to csv file'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        with open(kwargs['path'], 'w', newline='') as csvfile:
            attributes = ['Latitude',
                            'Longitude', 
            		    'Unique Squirrel ID', 
            		    'Shift', 
            		    'Date', 
            		    'Age', 
            		    'Primary Fur Color', 
            		    'Location',
                            'Specific Location',
                            'Running',
                            'Chasing',
                            'Climbing',
                            'Eating',
                            'Foraging',
                            'Other Activities',
                            'Kuks',
                            'Quaas',
                            'Moans',
                            'Tail Flags',
                            'Tail Twitches',
                            'Approaches',
                            'Indifferent',
                            'Runs From']
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            writer.writerow(attributes)
            for row in Squirrel.objects.all():
                writer.writerow([getattr(row, attribute) for attribute in attributes])
