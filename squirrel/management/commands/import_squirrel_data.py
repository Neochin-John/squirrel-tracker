import csv
from django.core.management.base import BaseCommand
from dateutil import parser
from squirrel.models import Sighting
from datetime import date
import re

class Command(BaseCommand):
    help = 'Import the squirrel csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_data.csv', help='file containing sighting details') 

    def handle(self, *args, **kwargs):
        path = kwargs['squirrel_data.csv']
        pattern = re.compile(r'(\d{2})(\d{2})(\d{4})')

        with open(path,'rt',encoding='UTF-8') as fp:
            reader = csv.DictReader(fp)
            for item in reader:
                month, day, year = pattern.match(item['Date']).groups()
                obj = Sighting()
                obj.longitude = float(item['X'])
                obj.latitude = float(item['Y'])
                obj.unique_squirrel_id = item['Unique Squirrel ID']
                obj.shift = item['Shift']
                obj.date = date(int(year), int(month), int(day))
                obj.age = item['Age']
                obj.primary_fur_color = item['Primary Fur Color']
                obj.location = item['Location']
                obj.specific_location = item['Specific Location']
                obj.running = True if item['Running'] == 'true' else False
                obj.chasing = True if item['Chasing'] == 'true' else False
                obj.climbing = True if item['Climbing'] == 'true' else False
                obj.eating = True if item['Eating'] == 'true' else False
                obj.foraging = True if item['Foraging'] == 'true' else False
                obj.other_activities = item['Other Activities']
                obj.kuks = True if item['Kuks'] == 'true' else False
                obj.quaas = True if item['Quaas'] == 'true' else False
                obj.moans = True if item['Moans'] == 'true' else False
                obj.tail_flags = True if item['Tail flags'] == 'true' else False
                obj.tail_twitches = True if item['Tail twitches'] == 'true' else False
                obj.approaches = True if item['Approaches'] == 'true' else False
                obj.indifferent = True if item['Indifferent'] == 'true' else False
                obj.runs_from = True if item['Runs from'] == 'true' else False
                    
                try:
                    obj.save()
                except Exception as e:
                    msg=f'ERROR:{e}at{obj.unique_squirrel_id}'
                    self.stdout.write(self.style.ERROR(msg))
