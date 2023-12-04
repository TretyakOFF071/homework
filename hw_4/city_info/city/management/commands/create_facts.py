from django.core.management import BaseCommand
from city.models import Facts

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Факты создаются')
        facts = [
            ('Статуя свободы','Каркас для статуи Свободы в США произведён из металла, добытого в Екатеринбурге.'),
            ('Метро','В России этот город стал третьим после Санкт-Петербурга и Москвы, где появился метрополитен.'),
            ('Название','Екатеринбург назван в честь Екатерины I')
        ]

        for fact in facts:
            new_fact = Facts.objects.create(title=fact[0], content=fact[1])

            new_fact.save()
        self.stdout.write(self.style.SUCCESS('Факты созданы'))