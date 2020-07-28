from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

class LoginAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user', email='test@gmail.com', password='pass1234')
        self.login_url = reverse('login')

    def test_login(self):
        data = {
            'email': self.user.email,
            'password': 'pass1234'
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)

    def test_fail_login(self):
        data = {
            'email': self.user.email,
            'password': 'failpassword'
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
