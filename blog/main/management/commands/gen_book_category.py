import random

from django.core.management import BaseCommand
from faker import Faker

from main.models import Book, Author

from main.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(10):
            Author(name=fake.name(), email=fake.email(), age=random.randint(1, 100)).save()

        categories = ['Adventure', 'Detective', 'Mystery']
        for category in categories:
            Category(name=category).save()

        for i in range(20):
            author = Author.objects.order_by('?').last()
            category = Category.objects.order_by('?').first()
            Book(title=f'Title {i}', author=author, category=category).save()
