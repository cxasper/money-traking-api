from random import randint
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.api.builders import meta_data_specific


class CreateAccountAPITestCase(APITestCase):
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
        self.client.force_authenticate(user=user)

    def test_ok_create(self):
        res = self.client.post(
            self.base_url,
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
