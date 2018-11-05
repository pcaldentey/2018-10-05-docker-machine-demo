from rest_framework import generics
from .models import Client
from .serializers import ClientSerializer


class ClientList(generics.ListCreateAPIView):
    """
    List and create clients.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a client instance.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
