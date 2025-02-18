import json
import os

from django.core.management.base import BaseCommand
from django.db import transaction

from missions.models import Mission
from parsec_capitalism.settings import BASE_DIR
from ships.models import Perk, Ship


class Command(BaseCommand):
    help = 'Command that loads basic game objects from csv'

    def load_ships(self, file_path):
        """Load ships' data from the json file"""
        with open(file_path) as file:
            data = json.load(file)
            ship_dict = data['Ships']
            ships = [Ship(**ship_data) for ship_data in ship_dict]
            Ship.objects.bulk_create(ships)
            self.stdout.write(f'Successfully loaded {len(ship_dict)} ship object(s)')

    def load_perks(self, file_path):
        """Load perks' data from the json file"""
        with open(file_path) as file:
            data = json.load(file)
            perk_dict = data['Perks']
            perks = [Perk(**perk_data) for perk_data in perk_dict]
            Perk.objects.bulk_create(perks)
            self.stdout.write(f'Successfully loaded {len(perk_dict)} perk object(s)')

    def load_missions(self, file_path):
        """Load perks' data from the json file"""
        with open(file_path) as file:
            data = json.load(file)
            mission_dict = data['Missions']
            missions = [Mission(**mission_data) for mission_data in mission_dict]
            Mission.objects.bulk_create(missions)
            self.stdout.write(
                f'Successfully loaded {len(mission_dict)} mission object(s)'
            )

    def handle(self, *args, **kwargs):
        directory = os.path.join(BASE_DIR, 'static/game_data/')

        try:
            with transaction.atomic():
                self.stdout.write('Deleting existing data')
                Ship.objects.all().delete()
                Mission.objects.all().delete()
                Perk.objects.all().delete()

                for file in os.listdir(directory):
                    file_path = os.path.join(directory, file)

                    if file.endswith('ships.json'):
                        self.load_ships(file_path)

                    if file.endswith('missions.json'):
                        self.load_missions(file_path)

                    if file.endswith('perks.json'):
                        self.load_perks(file_path)
                self.stdout.write(self.style.SUCCESS('All data is loaded'))

        except Exception as e:
            self.stdout.write(f'Error loading data: {e}')
