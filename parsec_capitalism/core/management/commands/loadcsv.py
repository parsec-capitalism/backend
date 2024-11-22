from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'smth'

    def handle(self, *args, **kwargs):
        print(self.help)
