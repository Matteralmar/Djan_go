from random import random

from django.core.management import BaseCommand
from faker import Faker

from main.models import Book, Author

from main.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(10):
            Author(name=fake.name(), email=fake.email(), age=100).save()

        for a in range(10):
            Category(name=fake.name())

        for i in range(10):
            author = Author.objects.order_by('?').last()
            Book(title=f'Title {i}', author=author).save()
