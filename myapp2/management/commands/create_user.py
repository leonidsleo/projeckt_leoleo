from typing import Any
from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = 'Добавить пользователя'


    def handle(self, *args, **kwargs):
        user = User(name='Jhon2', email='john33@mail.ru', password='1sew4er5k2retfd22', age=21)
        user.save()
        self.stdout.write(f'{user}')
    