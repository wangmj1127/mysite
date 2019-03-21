from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.utils import timezone
import datetime

from .models import UserAccount


# Create your tests here.

class AccountTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

    def test_validate_register(self):
        self.assertEquals(0, len(UserAccount.objects.filter(email='user123@user.com')))
        response = self.client.post(reverse('account:register'), {
            'username': 'user1233',
            'email': 'user123@user.com',
            'password1': 'password123!q@wE#R$T',
            'password2': 'password123!q@wE#R$T',
        })

        self.assertEquals(1, len(UserAccount.objects.filter(email='user123@user.com')))

        self.client.login(username='user1233', password='password123!q@wE#R$T')
