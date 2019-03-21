from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from .models import Note, NoteComment
from apps.accounts.models import UserAccount


# Create your tests here.

class ModelTest(TestCase):
    # set up
    def setUp(self):
        UserAccount.objects.create(username="testuser", password="test123", email="test@test.com")
        Note.objects.create(content="test", cover="image/2019/03/p22.jpg", like_count=12)
        NoteComment.objects.create(user_id=1, note_id=1, comment="test")

    # Test if the Note model is created correctly
    def test_note_model(self):
        result = Note.objects.get(cover="image/2019/03/p22.jpg")
        self.assertEqual(result.content, "test")
        self.assertEqual(result.like_count, 12)

    # Test if the NoteComment model is created correctly
    def test_comment_model(self):
        result = NoteComment.objects.get(note_id=1)
        self.assertEqual(result.user.username, "testuser")
        self.assertEqual(result.note.content, "test")
        self.assertEqual(result.note.like_count, 12)

    # Test the response of the home page
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # Test the response of the edit_note page
    def test_edit_note(self):
        response = self.client.get('/edit_note/')
        self.assertEqual(response.status_code, 200)

    # Test the response of the note_detail page
    def test_note_detail(self):
        response = self.client.get('/note_detail/1/')
        self.assertEqual(response.status_code, 200)


class ValidateNote(TestCase):
    # set up
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

    # Validate the creation of notes
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




