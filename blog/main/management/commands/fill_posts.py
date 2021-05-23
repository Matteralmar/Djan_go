
import requests
from bs4 import BeautifulSoup
from django.core.management import BaseCommand

from main.soup_service import soup_service


class Command(BaseCommand):
    def handle(self, *args, **options):
        url = 'https://doroshenkoaa.ru/med/'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = []
        titles = []
        soup_service(links, soup, titles)



