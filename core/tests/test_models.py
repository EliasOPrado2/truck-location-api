from django.test import TestCase
from core.models import Address, Route, TruckDriver


class TestModels(TestCase):

    def setUp(self):

        self.truck_driver = TruckDriver.objects.create(
            name='John Doe',
            age=32,
            sex=0,
            has_truck=True,
            cnh_type=1,
            is_loaded=False,
            truck_type=1
        )
        self.truck_driver.save()

        self.address = Address.objects.create(
            address='Avenida paulista 66',
            neighborhood="bela vista",
            city="Sao Paulo",
            state="SP",
            postcode="01310-000",
            country="Brasil",
            latitude=-23.5704923,
            longitude=-46.6449193
        )
        self.address.save()

        self.route = Route.objects.create(
            truck_driver=self.truck_driver,
            origin=self.address,
            destination=self.address,
            distance=23,
            is_active=False
        )
        self.route.save()

    def test_address(self):
        """
        Test data insertion into Address model.
        """
        self.assertEqual(self.address.address, 'Avenida paulista 66')
        self.assertEqual(self.address.neighborhood, "bela vista")
        self.assertEqual(self.address.city, "Sao Paulo")
        self.assertEqual(self.address.state, "SP")
        self.assertEqual(self.address.postcode, "01310-000")
        self.assertEqual(self.address.country, "Brasil")
        self.assertEqual(self.address.latitude, -23.5704923)
        self.assertEqual(self.address.longitude, -46.6449193)
        self.assertNotEqual(self.address.longitude, "-46.6449193")
        self.assertNotEqual(self.address.longitude, "-46.6449193")

    def test_route_model(self):
        """
        Test data insertion into Route model.
        """
        self.assertEqual(self.route.truck_driver, self.truck_driver)
        self.assertEqual(self.route.origin, self.address)
        self.assertEqual(self.route.destination, self.address)
        self.assertEqual(self.route.distance, 23)
        self.assertEqual(self.route.is_active, False)

    def test_truck_driver_model(self):
        """
        Test data insertion into Route model.
        """
        self.assertEqual(self.truck_driver.name,'John Doe')
        self.assertEqual(self.truck_driver.age, 32)
        self.assertEqual(self.truck_driver.sex, 0)
        self.assertEqual(self.truck_driver.has_truck, True)
        self.assertEqual(self.truck_driver.cnh_type, 1)
        self.assertEqual(self.truck_driver.is_loaded, False)
        self.assertEqual(self.truck_driver.truck_type, 1)