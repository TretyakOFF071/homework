from django.core.management import BaseCommand
from city.models import Management

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Руководители создаются')
        managers = [
            ('Орлов Алексей Валерьевич', 'Глава Екатеринбурга'),
            ('Сутягин Игорь Евгеньевич', 'Первый заместитель Главы Екатеринбурга'),
            ('Фадеева Марина Сергеевна', 'Руководитель аппарата Администрации города Екатеринбурга')
    ]

        for manager in managers:
            new_man = Management.objects.create(name=manager[0], title=manager[1])

            new_man.save()

        self.stdout.write(self.style.SUCCESS('Руководители созданы'))