from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pet
from .services import get_pet_query, normalize_pet_query_request

from .serializer import PetSerializer
from .init_data import load_all
from .database import load_xlsx
from django.conf import settings


# Create your views here.

class PetsView(APIView):

    def post(self, request, *args, **kwargs):
        # load_all()
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        # load_xlsx()
        request_data = request.data
        norm_req = normalize_pet_query_request(request_data)
        ser = PetSerializer(get_pet_query(norm_req), many=True)
        return Response(data=ser.data)


class TestAPIView(APIView):

    def post(self, request, *args, **kwargs):
        request_data = request.data
        norm = normalize_pet_query_request(request_data)


class ImageApiView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.GET
        if data['pet'] == 'dogs':
            return Response(data=[f'{settings.STATIC_URL}/img/dogs/{i}.jpg' for i in range(20)])
        else:
            return Response(data=[f'{settings.STATIC_URL}/img/cats/{i}.jpg' for i in range(20)])
