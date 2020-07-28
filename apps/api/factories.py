import factory
from faker import Faker
from random import randint
from django.contrib.auth.models import User
from apps.api.models import Account, Transaction

fake = Faker()
profile = fake.simple_profile()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = profile['mail']
    username = profile['mail']


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    user = factory.SubFactory(UserFactory)
    currency_id = randint(1, 3)
    name = factory.Faker('job')
    display_name = factory.Faker('catch_phrase')
    description = factory.Faker('paragraph')


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    account = factory.SubFactory(AccountFactory)
    name = factory.Faker('job')
    display_name = factory.Faker('catch_phrase')
    description = factory.Faker('paragraph')
    type_id = randint(1, 2)
    amount = randint(10000, 1000000)/100
