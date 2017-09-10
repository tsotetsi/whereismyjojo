from django.test import TestCase, Client
from rest_framework import status

from.factories import UserFactory


class UserModelTests(TestCase):
    def setUp(self):
        super(UserModelTests, self).setUp()
        self.client = Client()
        self.user = UserFactory()

    def test_user_view_set_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_user_view_set_retrieve(self):
        response = self.client.get('/api/users/' + self.user.id + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_results = {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'is_staff': self.user.is_staff
        }
        self.assertEqual(response.data[0], expected_results)

    def test_user_view_set_create(self):
        pass
