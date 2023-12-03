from django.core.management import BaseCommand
from city.models import News

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Создаются новости..')

    news = [
        ('Снегопад', 'Выпало очень много снега, на дорогах огромные пробки'),
        ('Проишествие', 'Недавно в ТРЦ Гринвич неизвестные устроили перестрелку'),
        ('Похолодание', 'Скоро наступят морозы, одевайтесь теплее!')
    ]

    for i_new in news:
        new_novost = News.objects.create(title=i_new[0], content=i_new[1])

        new_novost.save()

    self.stdout.write(self.style.SUCCESS('Новости созданы'))