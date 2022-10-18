from urllib import response
from apps.juber.models import Model
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from.factories import ModelFactory, UserFactory


class UserModelTests(APITestCase):
    def setUp(self):
        super(UserModelTests, self).setUp()
        self.client = APIClient()
        self.user = UserFactory()

    def test_user_view_set_list(self):
        """
        Ensure user can retrieve all users.
        """
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_user_view_set_retrieve(self):
        """
        Ensure user can retrieve a specific user.
        """
        response = self.client.get('/api/users/' + str(self.user.id) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_results = {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'is_staff': self.user.is_staff
        }
        self.assertEqual(response.data, expected_results)

    def test_user_view_set_create(self):
        """
        Ensure a new user can be created by the admin.
        """
        data = {
            'username': 'user_1',
            'email': 'user_1@gmail.com',
            'is_staff': False
        }
        new_user = User.objects.create_superuser('admin_1', 'admin_1@admin.com', 'admin_1')
        self.client.force_login(User.objects.get(username='admin_1'))

        response = self.client.post('/api/users/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(new_user, User.objects.get(username='admin_1'))


class ModelTests(APITestCase):

    api_url = "/api/models/"

    def setUp(self) -> None:
        super(ModelTests, self).setUp()
        self.client = APIClient()
        self.model = ModelFactory()
    
    def test_model_view_set_list(self):
        """
        Ensure user can retrieve all vehicles models
        """
        response = self.client.get(self.api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_model_view_set_retrieve(self):
        """
        Ensure a specific vehicle moel can be retrieved.
        """
        response = self.client.get(self.api_url + str(self.model.id) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_results = {
            'id': self.model.id,
            'name': self.model.name,
            'description': self.model.description
        }
        self.assertEqual(response.data, expected_results)

    def test_model_view_set_create(self):
        """
        Ensure a new vehicle model can be created by the admin
        """
        data = {
            'name': 'Benz 2',
            'description': 'Double axle'
        }
        new_admin = User.objects.create_superuser('admin_2', 'admin_2@admin.com', 'admin_2')
        self.client.force_login(new_admin)

        response = self.client.post(self.api_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 3)

