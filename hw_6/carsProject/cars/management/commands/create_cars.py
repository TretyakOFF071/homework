from django.core.management.base import BaseCommand
from cars.models import Cars

class Command(BaseCommand):
    def handle(self, *args, **options):
        cars = [
            ('toyota', 'Corolla', 180, 2018),
            ('honda', 'Accord', 200, 2019),
            ('renault', 'Clio', 130, 2020)
        ]

        for car in cars:
            new_car = Cars.objects.get(brand=car[0], model=car[1], horsepower=car[2], year=car[3])
            new_car.save()
        self.stdout.write(self.style.SUCCESS('Автомобили созданы'))