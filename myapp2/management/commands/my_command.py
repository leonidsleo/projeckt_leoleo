from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Print 'Привет мир' to output"

    def handle(self, *args, **kwargs):
        self.stdout.write('Привет мир')


    