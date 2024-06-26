# команда для заполнения таблиц фэковыми данными
#  заполняем таблицы autor и post

from django.core.management.base import BaseCommand
from myapp2.models import Autor, Post


class Command(BaseCommand):
    help = "Генерация фэйковых данных"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User age')
    

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count+1):
            autor = Autor(name=f'Name{i}', email=f'mail{i}@mail.ru')
            autor.save()
            for j in range(1, count+1):
                post = Post(title=f'Title{j}', content=f'Текст от автора {autor.name} номер {j} и тут какой то текст', autor=autor)
                post.save()