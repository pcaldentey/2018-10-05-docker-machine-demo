from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Client, ClientAccount, Store
from .serializers import ClientSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_client(dni="", name=""):
        if dni != "" and name != "":
            Client.objects.create(dni=dni, name=name)

    def setUp(self):
        # add test data
        self.create_client("123123123A", "Laura Pérez")
        self.create_client("321321321B", "Antonio López")
        ClientAccount.objects.create(client_id="321321321B")
        Store.objects.create(cif="111111111A", name="La tienda de los test",
                             account_status=Store.ENABLED_STATUS)
        self.create_client("213213213C", "José Martínez")
        self.create_client("312312312D", "Luisa Mercado")


class ClientsEndPointsTest(BaseViewTest):

    def test_register(self):
        """
        This test ensures that a client is saved in database
       when we make a POST request to the api/clients/ endpoint
        """
        # hit the API endpoint
        response = self.client.post('/api/clients/',
                                    {'dni': '432432432G',
                                     'name': 'Flor Sánchez'},
                                    format='json')
        # fetch the data from db
        expected = Client.objects.get(pk='432432432G')
        serialized = ClientSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_fails(self):
        """
        Checking validation errors in register
        """
        # Already in database
        response = self.client.post('/api/clients/',
                                    {'dni': '312312312D',
                                     'name': 'Flor Sánchez'},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # dni too short
        response = self.client.post('/api/clients/',
                                    {'dni': '312312D',
                                     'name': 'Flor Sánchez'},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # dni too long
        response = self.client.post('/api/clients/',
                                    {'dni': '312318768768767862D',
                                     'name': 'Flor Sánchez'},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_client(self):
        """
        This test checks GET request to the api/clients/
        endpoint
        """
        # hit the API endpoint
        response = self.client.get('/api/clients/123123123A/', format='json')
        # fetch the data from db
        expected = Client.objects.get(pk='123123123A')
        serialized = ClientSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/api/clients/123123123B/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list(self):
        """
        This test checks client listings GET request to the api/clients/
        endpoint
        """
        # hit the API endpoint
        response = self.client.get('/api/clients/', format='json')
        # fetch the data from db
        expected = Client.objects.all()
        serialized = ClientSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
