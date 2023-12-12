from django.core.management.base import BaseCommand
from app_headphones.models import Headphone

class Command(BaseCommand):

    def handle(self, *args, **options):

        headphones = [
            ('airpods_2', 'white','5 hours'),
            ('buds_4_pro', 'black','9 hours'),
            ('freebuds_2', 'white','7 hours')
        ]

        for headphone in headphones:
            new_headphone = Headphone.objects.create(model=headphone[0], color=headphone[1], charge=headphone[2])
            new_headphone.save()
        self.stdout.write(self.style.SUCCESS('Наушники созданы'))