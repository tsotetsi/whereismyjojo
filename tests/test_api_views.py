from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from.factories import UserFactory


class UserModelTests(APITestCase):
    def setUp(self):
        super(UserModelTests, self).setUp()
        self.client = APIClient()
        self.user = UserFactory()

    def test_user_view_set_list(self):
        """
        Ensure admin can retrieve all users.
        """
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_user_view_set_retrieve(self):
        """
        Ensure admin can retrieve a specific user.
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
        Ensure a new user can be created.
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
