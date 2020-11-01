from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from .services import get_pet_query, normalize_pet_query_request, get_pet_dict, api_normalize_pet_request
from .serializer import PetSerializer
from django.conf import settings
from .models import Pet


class PetsView(APIView):

    def post(self, request, *args, **kwargs):
        request_data = request.data
        norm_req = normalize_pet_query_request(request_data)
        ser = PetSerializer(get_pet_query(norm_req), many=True)
        return Response(data=ser.data)


class UpdateDetailPetView(RetrieveUpdateAPIView):
    queryset = Pet.objects
    serializer_class = PetSerializer


class TestAPIView(APIView):

    def post(self, request, *args, **kwargs):
        request_data = api_normalize_pet_request(request.data)
        pet_dict = get_pet_dict(request_data)
        return Response(data=pet_dict)


class ImageApiView(APIView):

    def get(self, request, *args, **kwargs):
        data = request.GET
        if data['pets'] == 'dogs':
            return Response(data=[f'{settings.STATIC_URL}img/dogs/{i}.jpg' for i in range(20)])
        else:
            return Response(data=[f'{settings.STATIC_URL}img/cats/{i}.jpg' for i in range(20)])
