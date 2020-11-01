from rest_framework.response import Response
from rest_framework.views import APIView
from .tests import create_card
from pet.models import Pet
from pet.init_data import load_all
from pet.database import load_xlsx


class AnimalCard(APIView):
    def get(self, request, *args, **kwargs):
        # load_all()
        # load_xlsx()
        pet = Pet.objects.get(accounting_card=191)
        path = create_card(pet)
        return Response({'source': path})


class Summary(APIView):
    ...


class Monitoring(APIView):
    ...
