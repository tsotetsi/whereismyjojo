from urllib import response
from apps.juber.models import Model
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from.factories import DriverFactory, ModelFactory, TripFactory, UserFactory, VehicleFactory


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
        Ensure a specific vehicle model can be retrieved.
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


class DriverModelTest(APITestCase):
    
    api_url = "/api/drivers/"

    def setUp(self) -> None:
        super(DriverModelTest, self).setUp()
        self.client = APIClient()
        self.driver = DriverFactory()
    
    def test_driver_view_set(self):
        """
        Ensure a user can retrieve all drivers
        """
        response = self.client.get(self.api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_driver_view_set_retrieve(self):
        """
        Ensure a specific driver can be retrieved.
        """
        response = self.client.get(self.api_url + str(self.driver.id) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_results = {
            'id': self.driver.id,
            'name': self.driver.name,
            'contact_number': self.driver.contact_number,
            'license_number': self.driver.license_number,
            'has_pdp': self.driver.has_pdp
        }
        self.assertEqual(response.data, expected_results)

    def test_driver_view_set_create(self):
        """
        Ensure a new driver can be created by the admin
        """
        data = {
            'name': 'Driver_2',
            'contact_number': '+273456789',
            'license_number': 'WPN1234ZP1',
            'has_pdp': True
        }
        new_admin = User.objects.create_superuser('admin_3', 'admin_3@admin.com', 'admin_3')
        self.client.force_login(new_admin)

        response = self.client.post(self.api_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 5)

class VehicleModelTest(APITestCase):
    
    api_url = "/api/vehicles/"

    def setUp(self) -> None:
        super(VehicleModelTest, self).setUp()
        self.client = APIClient()
        self.vehicle = VehicleFactory()
    
    def test_vehicle_view_set(self):
        """
        Ensure a user can retrieve all vehicles.
        """
        response = self.client.get(self.api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_vehicle_view_set_retrieve(self):
        """
        Ensure a specific vehicle can be retrieved.
        """
        response = self.client.get(self.api_url + str(self.vehicle.id) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_results = {
            'id': self.vehicle.id,
            'field_number': self.vehicle.field_number,
            'registration_number': self.vehicle.registration_number,
            'liters': self.vehicle.liters,
            'is_active': self.vehicle.is_active
        }
        self.assertEqual(response.data, expected_results)

    def test_driver_view_set_create(self):
        """
        Ensure a new vehicle can be created by the admin
        """
        model = ModelFactory()
        data = {
            'model_id': model.id,
            'field_number': 'BQP012DP',
            'registration_number': 'NKR0123MP',
            'liters': 40000,
            'is_active': True
        }
        new_admin = User.objects.create_superuser('admin_4', 'admin_4@admin.com', 'admin_4')
        self.client.force_login(new_admin)

        response = self.client.post(self.api_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 5)
