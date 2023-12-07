from django.core.management.base import BaseCommand
from app_writers.models import Writer, Book

class Command(BaseCommand):

    def handle(self, *args, **options):

        writers = [
            ('А́нджей Сапко́вский', ' 21 июня 1948'),
            ('Антон Чехов', '29 января 1860'),
            ('Михаил Булгаков', '15 мая 1891')
        ]
        books = [
            ('Ведьмак', '1986', 'А́нджей Сапко́вский', 1),
            ('Кровь эльфов', '1994', 'А́нджей Сапко́вский', 2),
            ('Владычица озера', '1999', 'А́нджей Сапко́вский', 3),
            ('Мастер и Маргарита', '1967', 'Михаил Булгаков', 4),
            ('Чайка', '1896', 'Антон Чехов', 5),
            ('Чугунный завет', '1897', 'Антон Чехов', 6),
            ('Собачье сердце', '1925', 'Михаил Булгаков', 7),
        ]

        for writer in writers:
            new_writer = Writer.objects.create(name=writer[0], birth_date=writer[1])
            new_writer.save()


        for book in books:
            writer = Writer.objects.get(name=book[2])
            new_book = Book.objects.create(title=book[0], publication_date=book[1], writer=writer, rank=book[3])
            new_book.save()

        self.stdout.write(self.style.SUCCESS('Писатели и книги созданы'))