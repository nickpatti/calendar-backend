from django.core.management.base import BaseCommand, CommandError
from users.models import Account, Staff, Customer
import uuid
import random
import requests
from bs4 import BeautifulSoup


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('a', type=int)
        parser.add_argument('s', type=int)
        parser.add_argument('c', type=int)

    def handle(self, *args, **options):

        URL = 'https://www.whattoexpect.com/baby-names/list/top-baby-names-for-boys/'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.select('ol > li')
        names = []

        for item in results:
            names.append(item.text)

        accounts_array = []
        array = []

        for accounts in range(options['a']):
            accounts_array.append(Account(email=(random.choice(names) + '.' + random.choice(names) + '@gmail.com'), date_of_birth='1994-01-26'))

        Account.objects.bulk_create(accounts_array)

        for objects in Account.objects.all():
            array.append(objects)

        for staff in range(options['s']):
            account = random.choice(array)
            Staff.objects.bulk_create([Staff(user=account)])
            array.remove(account)

        staff_objects = Staff.objects.all()

        for customers in range(options['c']):
            account = random.choice(array)
            Customer.objects.bulk_create([Customer(user=account, staff=random.choice(staff_objects))])
            array.remove(account)
