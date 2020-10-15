import csv
from django.core.management import BaseCommand
from dateutil import parser
from project.models import Squirrel
from datetime import date
import re

class Command(BaseCommand):
    help = 'Import the squirrel csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']

        pattern = re.compile(r'(\d{2})(\d{2})(\d{4})')

        with open(path, 'rt') as fp:
            reader = csv.reader(fp)
            unique_id = []
            for item in reader:
                if item['Unique Squirrel ID'] in unique_id:
                    continue
                else:
                    unique_id.append(item['Unique Squirrel ID'])
                    month, day, year = pattern.match(item['Date']).groups()
                    obj = Squirrel()
                    obj.latitude = float(item['X'])
                    obj.longitude = float(item['Y'])
                    obj.unique_squirrel_id = item['Unique Squirrel ID']
                    obj.shift = 'PM' if item['Shift'] == 'PM' else 'AM'
                    obj.date = date(int(year), int(month), int(day))
                    obj.age = item['Age']
                    obj.primary_fur_color = item['Primary Fur Color']
                    obj.location = item['Location']
                    obj.specific_location = item['Specific Location']
                    obj.running = True if item['Running'] == 'true' else False
                    obj.chasing = True item['Chasing'] == 'true' else False
                    obj.climbing = True item['Climbing'] == 'true' else False
                    obj.eating = True item['Eating'] == 'true' else False
                    obj.foraging = True item['Foraging'] == 'true' else False
                    obj.other_activities = item['Other Activities']
                    obj.kuks = True item['Kuks'] == 'true' else False
                    obj.quaas = True item['Quaas'] == 'true' else False
                    obj.moans = True item['Moans'] == 'true' else False
                    obj.tail_flags = True item['Tail flags'] == 'true' else False
                    obj.approaches = True item['Tail twitches'] == 'true' else False
                    obj.indifferent = True item['Indifferent'] == 'true' else False
                    obj.runs_from = True item['Runs from'] == 'true' else False
                    obj.save()

