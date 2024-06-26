from django.core.management.base import BaseCommand
from myapp2.models import Autor, Post


# class Command(BaseCommand):
#     help = "Поиск постов автора по id"

#     def add_arguments(self, parser):
#         parser.add_argument('pk', type=int, help='User id')
    

#     def handle(self, *args, **kwargs):
#         pk = kwargs['pk']
#         autor = Autor.objects.filter(pk=pk).first()
#         if autor is not None:
#             posts = Post.objects.filter(autor=autor)
#             intro = f'Все посты от {autor.name}\n'
#             text = '\n'.join(post.content for post in posts)
#             self.stdout.write(f'{intro}{text}')


"""вариант запроса не обращаясь к таблице autor"""


class Command(BaseCommand):
    help = "Поиск постов автора по id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User id')
    

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        posts = Post.objects.filter(autor__pk=pk)
        intro = f'Все посты\n'
        # text = '\n'.join(post.content for post in posts)
        """после создания метода get_summary в моделе post теперь общаемся к этому методу"""
        text = '\n'.join(post.get_summary() for post in posts)
        self.stdout.write(f'{intro}{text}')