import csv
import os

from django.core.management.base import BaseCommand

from missions.models import Missions
from parsec_capitalism.settings import BASE_DIR
from ships.models import Ship


class Command(BaseCommand):
    help = 'Command that loads basic game objects from csv'

    def handle(self, *args, **kwargs):
        Ship.objects.all().delete()

        directory = os.path.join(BASE_DIR, 'static/game_data/')
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            file_path = os.path.join(directory, file)

            if 'ships' in filename:
                with open(file_path) as csvfile:
                    ship_db = csv.reader(csvfile, delimiter=',')
                    next(ship_db, None)
                    for row in ship_db:
                        Ship.objects.create(
                            slug=row[0],
                            name=row[1],
                            price=row[2],
                            cargo_volume=row[3],
                            cargo_weight=row[4],
                            range=row[5],
                        )

            if 'missions' in filename:
                with open(file_path) as csvfile:
                    mission_db = csv.reader(csvfile, delimiter=',')
                    next(mission_db, None)
                    for row in mission_db:
                        Missions.objects.create(
                            codename=row[0],
                            expansion=row[1],
                            reward=row[2],
                            summary=row[3],
                            duration=row[4],
                            distance=row[5],
                            volume=row[6],
                            weight=row[7],
                        )
