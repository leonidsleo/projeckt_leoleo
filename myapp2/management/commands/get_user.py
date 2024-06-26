from django.core.management.base import BaseCommand
from myapp2.models import User

"""# использование метода get
# есть недостаток при отсутствии в базе данных будет выдавать не понятные
# пользователю ошибки
# поэтому используем filter"""
# class Command(BaseCommand):
#     help = "Поиск пользователя по id"

#     def add_arguments(self, parser):
#         parser.add_argument('id', type=int, help='User ID')
    

#     def handle(self, *args, **kwargs):
#         id = kwargs['id']
#         user = User.objects.get(id=id)
#         self.stdout.write(f'{user}')


"""использование метода filter"""
class Command(BaseCommand):
    help = "Поиск пользователя по id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID') # вместо id используем pk
    

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')

"""параметры фильтрации смотри в metodichka строка 319"""