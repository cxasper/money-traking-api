from random import randint
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.api.builders import meta_data_specific
from apps.api.models import Account


class CreateTransactionAPITestCase(APITestCase):
    """docstring for ClassName"""

    base_url = '/api/accounts/{}/transactions/'
    valid_payload = {
        "amount": randint(100, 300)/100,
        "description": "Transaction de ejemplo",
        "type": randint(1, 2),
    }

    def setUp(self):
        meta_data_specific(['currency', 'type_transactions'])
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

    def test_ok_create(self):
        res = self.client.post(
            self.base_url.format(self.account.id),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
