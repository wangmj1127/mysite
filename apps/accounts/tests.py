from django.test import TestCase, Client, RequestFactory
from django.urls import reverse


from .models import UserAccount


# Create your tests here.

class AccountTest(TestCase):

    # set up
    def setUp(self):
        UserAccount.objects.create(username="testuser", password="test123", email="test@test.com")
        self.client = Client()
        self.factory = RequestFactory()

    # Test if UserAccount model is created correctly
    def test_useraccount_model(self):
        result = UserAccount.objects.get(username="testuser")
        self.assertEqual(result.password, "test123")
        self.assertEqual(result.email, "test@test.com")

    # validate the registration
    def test_validate_register(self):
        self.assertEquals(0, len(UserAccount.objects.filter(email='user123@user.com')))
        response = self.client.post(reverse('account:register'), {
            'username': 'user1233',
            'email': 'user123@user.com',
            'password1': 'password123!q@wE#R$T',
            'password2': 'password123!q@wE#R$T',
        })

        self.assertEquals(1, len(UserAccount.objects.filter(email='user123@user.com')))
        # Test if user1233 can login in successfully
        self.client.login(username='user1233', password='password123!q@wE#R$T')
        # Test if user1233 can access in to account page after login
        response = self.client.get('/account/')
        self.assertEqual(response.status_code, 200)

    # Test the response of the login page
    def test_login_page(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    # Test the response of the register page
    def test_register_page(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)




