from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Вывести всех пользователей"

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        self.stdout.write(f'{users}')
