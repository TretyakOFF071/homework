from django.core.management import BaseCommand
from city.models import Contacts


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Контакты содзаются')
        contacts = [
            ('Номер 1','+799143541635000'),
            ('Номер 2', '484646546541633'),
            ('Номер 3', '135968748641633')
        ]

        for contact in contacts:
            new_contact = Contacts.objects.create(name=contact[0], number=contact[1])

            new_contact.save()

        self.stdout.write(self.style.SUCCESS('Контакты созданы'))