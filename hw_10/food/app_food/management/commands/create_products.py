from django.core.management import BaseCommand
from app_food.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Создаются продукты...')

        products = [
            ('Яблоко', 120.10, 'Очень вкусное яблоко'),
            ('Апельсин', 130.10, 'Очень вкусный апельсин'),
            ('Клубника', 520.10, 'Очень кислая клубника'),
        ]
        for product in products:
            new_product = Product.objects.create(name=product[0],
                                                 price=product[1], description=product[2])
            new_product.save()
            self.stdout.write(f'Продукт {product[0]} создан.')
        self.stdout.write(self.style.SUCCESS('Продукты созданы'))
