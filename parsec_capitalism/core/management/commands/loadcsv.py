import csv
import os

from django.core.management.base import BaseCommand
from django.db import transaction

from missions.models import Mission
from parsec_capitalism.settings import BASE_DIR
from ships.models import Ship


class Command(BaseCommand):
    help = 'Command that loads basic game objects from csv'

    def load_ships(self, file_path):
        """Load ships' data from the csv file"""
        with open(file_path) as csvfile:
            ship_db = csv.reader(csvfile, delimiter=',')
            next(ship_db, None)
            ships = [
                Ship(
                    slug=row[0],
                    name=row[1],
                    price=row[2],
                    cargo_volume=row[3],
                    cargo_weight=row[4],
                    range=row[5],
                )
                for row in ship_db
            ]
            Ship.objects.bulk_create(ships)
            self.stdout.write(f'Successfully loaded {len(ships)} ships object(s)')

    def load_missions(self, file_path):
        """Load missions' data from the csv file"""
        with open(file_path) as csvfile:
            mission_db = csv.reader(csvfile, delimiter=',')
            next(mission_db, None)
            missions = [
                Mission(
                    codename=row[0],
                    expansion=row[1],
                    reward=row[2],
                    summary=row[3],
                    duration=row[4],
                    distance=row[5],
                    volume=row[6],
                    weight=row[7],
                )
                for row in mission_db
            ]
            Mission.objects.bulk_create(missions)
            self.stdout.write(f'Successfully loaded {len(missions)} missions object(s)')

    def handle(self, *args, **kwargs):
        directory = os.path.join(BASE_DIR, 'static/game_data/')

        try:
            with transaction.atomic():
                self.stdout.write('Deleting existing data')
                Ship.objects.all().delete()
                Mission.objects.all().delete()

                for file in os.listdir(directory):
                    file_path = os.path.join(directory, file)

                    if file.endswith('ships.csv'):
                        self.load_ships(file_path)

                    if file.endswith('missions.csv'):
                        self.load_missions(file_path)
                self.stdout.write(self.style.SUCCESS('Data successfully loaded'))

        except Exception as e:
            self.stdout.write(f'Error loading data: {e}')
