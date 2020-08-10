from random import randint
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.api.factories import AccountFactory
from apps.api.builders import meta_data_specific
from apps.api.models import Account


class ShowAccountAPITestCase(APITestCase):
    """docstring for ClassName"""

    base_url = '/api/accounts/{}/'

    def setUp(self):
        meta_data_specific(['currency'])
        user = User.objects.create_user(
            username='test_user',
            email='test@gmail.com',
            password='pass1234',
        )
        account_data = {
            "currency_id": randint(1, 3),
            "user_id": user.id,
            "name": "Account Test",
            "display_name": "Cuenta de ejemplo",
            "description": "Aquí manejo mi dinero personal",
        }
        self.account = Account.objects.create(**account_data)
        self.client.force_authenticate(user=user)

    def test_ok_show(self):
        res = self.client.get(
            self.base_url.format(self.account.id)
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
