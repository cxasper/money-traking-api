from random import randint
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.api.factories import AccountFactory
from apps.api.builders import meta_data_specific


class ListAccountAPITestCase(APITestCase):
    """docstring for ClassName"""

    base_url = reverse('list-accounts')
    valid_payload = {
        "currency": randint(1, 3),
        "name": "Account Test",
        "display_name": "Cuenta de ejemplo",
        "description": "Aquí manejo mi dinero personal",
    }

    def setUp(self):
        meta_data_specific(['currency'])
        user = User.objects.create_user(
            username='test_user',
            email='test@gmail.com',
            password='pass1234',
        )
        user_accounts = [AccountFactory(user=user) for _ in range(10)]
        other_account = AccountFactory()
        self.client.force_authenticate(user=user)

    def test_ok_list(self):
        res = self.client.get(self.base_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 10)
