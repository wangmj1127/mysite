from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.utils import timezone as datetime

from .models import Note
from apps.accounts.models import UserAccount


# Create your tests here.

class NoteTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

    def test_validate_note(self):
        self.assertEquals(0, len(UserAccount.objects.filter(email='user123@user.com')))
        response = self.client.post(reverse('account:register'), {
            'username': 'user1233',
            'email': 'user123@user.com',
            'password1': 'password123!q@wE#R$T',
            'password2': 'password123!q@wE#R$T',
        })
        self.client.login(username='user1233', password='password123!q@wE#R$T')

        response = self.client.post(reverse('note:store_note'), {
            'notePic': 'https://img.xiaohongshu.com/avatar/5b29aee714de415ff9964312.jpg@80w_80h_90q_1e_1c_1x.jpg',
            'noteContent': 'test',
        })

        self.assertEquals(1, len(Note.objects.filter(content='test')))
