import csv
from django.core.management.base import BaseCommand

from squirrel.models import Sighting
from datetime import date
import re

class Command(BaseCommand):
    help = 'Import the squirrel csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_data.csv', help='file containing sighting details') 

    def handle(self, *args, **kwargs):
        path = kwargs['squirrel_data.csv']

        with open(path, 'rt') as fp:
            reader = csv.DictReader(fp)
            for item in reader:
                obj = Sighting()
                obj.longitude = float(item['X'])
                obj.latitude = float(item['Y'])
                obj.unique_squirrel_id = item['Unique Squirrel ID']
                obj.shift = item['Shift']
                obj.date = item['Date']
                obj.age = item['Age']
                obj.primary_fur_color = item['Primary Fur Color']
                obj.location = item['Location']
                obj.specific_location = item['Specific Location']
                obj.running = True if item['Running'] == 'TRUE' else False
                obj.chasing = True if item['Chasing'] == 'TRUE' else False
                obj.climbing = True if item['Climbing'] == 'TRUE' else False
                obj.eating = True if item['Eating'] == 'TRUE' else False
                obj.foraging = True if item['Foraging'] == 'TRUE' else False
                obj.other_activities = item['Other Activities']
                obj.kuks = True if item['Kuks'] == 'TRUE' else False
                obj.quaas = True if item['Quaas'] == 'TRUE' else False
                obj.moans = True if item['Moans'] == 'TRUE' else False
                obj.tail_flags = True if item['Tail flags'] == 'TRUE' else False
                obj.approaches = True if item['Tail twitches'] == 'TRUE' else False
                obj.indifferent = True if item['Indifferent'] == 'TRUE' else False
                obj.runs_from = True if item['Runs from'] == 'TRUE' else False
                 
                obj.save()
                    
                msg=f'You are importing from {path}'
                self.stdout.write(self.style.SUCCESS(msg))
