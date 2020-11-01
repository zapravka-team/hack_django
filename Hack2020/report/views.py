from rest_framework.response import Response
from rest_framework.views import APIView
from .service import create_card
from pet.models import Pet


class AnimalCard(APIView):
    def get(self, request, *args, **kwargs):
        data = request.GET['accounting_car']
        pet = Pet.objects.get(accounting_card=data)
        path = create_card(pet)
        return Response({'source': path})


class Summary(APIView):
    ...


class Monitoring(APIView):
    ...
