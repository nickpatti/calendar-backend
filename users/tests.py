from knox.models import AuthToken
from rest_framework.test import APIRequestFactory, APIClient
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from .api import LoginAPI, RegisterAPI, UserAPI


class LoginAPITest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='user@foo.com', email='user@foo.com', password='top_secret')
        self.token = AuthToken.objects.create(user=self.user)

    def test_token_auth(self):
        request = self.factory.post('/api/auth/login', {'username': 'user@foo.com', 'email': 'user@foo.com', 'password': 'top_secret', 'token': self.token})
        view = LoginAPI.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        self.client.force_authenticate(self.user)
        request = self.client.get('/api/auth/user')
        self.assertEqual(request.status_code, 200)
