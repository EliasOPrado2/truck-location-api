import json
from rest_framework import status
from django.utils import timezone
from django.http import response
from django.urls import reverse
from core.models import Address, Route, TruckDriver
from rest_framework.test import APIClient, APITestCase

class TestAPI(APITestCase):

    def setUp(self):

        self.truck_driver = TruckDriver.objects.create(
            name='John Doe',
            age=32,
            sex=0,
            has_truck=True,
            cnh_type=1,
            is_loaded=True,
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

        self.address2 = Address.objects.create(
            address='Rua valdemar de paula ferreira',
            neighborhood="Jardim presidente dutra",
            city="Guarulhos",
            state="Sao Paulo",
            postcode="",
            country="Brasil",
            latitude=-23.4214942,
            longitude=-46.4340267
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

        self.address_data = {
            "address": "Rua valdemar de paula ferreira",
            "neighborhood": "Jardim presidente dutra",
            "city": "guarulhos",
            "state": "Sao Paulo",
            "postcode": "",
            "country": "Brasil"
        }

        self.truck_driver_data = {
            "id": 1,
            "name": "Elias Prado",
            "age": 32,
            "sex": 0,
            "has_truck": True,
            "cnh_type": "1",
            "is_loaded": True,
            "truck_type": 1
        }


        self.url_address_list = reverse('core:addresses-list')
        self.url_address_detail = reverse('core:addresses-detail',
                                        kwargs={'pk': self.address.pk})

        # this endpoint does not have post, delete, update and patch methods.
        self.url_route_list = reverse('core:routes-list')

        self.url_truck_driver_list = reverse('core:truck-drivers-list')
        self.url_truck_driver_detail = reverse('core:truck-drivers-detail',
                                        kwargs={'pk': self.truck_driver.pk})

    def test_get_addresses(self):
        """GET method for Address endpoint"""
        response = self.client.get(self.url_address_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_address(self):
        """ Test POST method for Address endpoint"""
        response = self.client.post(
            self.url_address_list, self.address_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_destination(self):
        """ Test PUT method for Address endpoint"""
        data = {
            "address": "Avenida paulista  66",
            "neighborhood": "bela vista",
            "city": "Sao Paulo",
            "state": "SP",
            "postcode": "01310-000",
            "country": "Brasil"
        }

        response = self.client.put(
            self.url_address_detail, data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_address(self):
        """ Test DELETE method for Destination endpoint"""
        response = self.client.delete(
            self.url_address_detail, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_truck_driver(self):
        """GET method for TruckDriver endpoint"""
        response = self.client.get(self.url_truck_driver_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_truck_driver(self):
        """ Test POST method for TruckDriver endpoint"""
        response = self.client.post(
            self.url_truck_driver_list, self.truck_driver_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_truck_driver(self):
        """ Test PUT method for TruckDriver endpoint"""
        data = {
            "id": 1,
            "name": "Elias Oliveira Prado",
            "age": 31,
            "sex": 0,
            "has_truck": True,
            "cnh_type": "1",
            "is_loaded": True,
            "truck_type": 1
        }

        response = self.client.put(
            self.url_truck_driver_detail, data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_truck_driver(self):
        """ Test DELETE method for TruckDriver endpoint"""
        response = self.client.delete(
            self.url_truck_driver_detail, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_loaded_truck_drivers(self):
        """Get all the loaded drivers"""
        response = self.client.get('/api/truck-drivers/', {'is_loaded': True})
        truck_driver_data = dict(response.data['results'][0])
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.truck_driver.is_loaded, truck_driver_data['is_loaded'])

    def test_truck_drivers_who_have_truck(self):
        """Get all the drivers who have truck"""
        response = self.client.get('/api/truck-drivers/', {'has_truck': True})
        truck_driver_data = dict(response.data['results'][0])
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.truck_driver.is_loaded, truck_driver_data['has_truck'])

    def test_get_route(self):
        truck_driver_id = self.truck_driver.id
        response = self.client.get(f"/api/truck-drivers/{truck_driver_id}/routes/")

        self.assertTrue(dict(response.data['results'][0]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_route(self):

        data= {
            "origin": self.address2,
            "destination": self.address2,
        }
        client = APIClient()
        truck_driver_id = self.truck_driver.id
        route_id = self.route.id
        response = client.put(f"/api/truck-drivers/{truck_driver_id}/routes/{route_id}", data, 'json')
        response2 = self.client.get(f"/api/truck-drivers/{truck_driver_id}/routes/")

        print("ROUTE -->",response.data)