from django.core.management.base import BaseCommand
from cars.models import Toyota, Honda, Renault

class Command(BaseCommand):

    def handle(self, *args, **options):

        Toyota.objects.create(model='Corolla', horsepower=140, year=2019)
        Toyota.objects.create(model='Сamry', horsepower=250, year=2021)

        Honda.objects.create(model='Civic', horsepower=150, year=2018)
        Honda.objects.create(model='Accord', horsepower=200, year=2020)

        Renault.objects.create(model='Clio', horsepower=130, year=2017)
        Renault.objects.create(model='Megane', horsepower=160, year=2019)

        self.stdout.write(self.style.SUCCESS('Автомобили добавлены'))