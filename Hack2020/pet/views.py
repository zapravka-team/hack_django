from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pet
from .services import get_pet_query, normalize_pet_query_request

from .serializer import PetSerializer
from .init_data import load_all
from .database import load_xlsx
import xlrd


# Create your views here.

class PetsView(APIView):

    def post(self, request, *args, **kwargs):
        load_all()
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        load_xlsx()
        request_data = request.data
        norm_req = normalize_pet_query_request(request_data)
        ser = PetSerializer(get_pet_query(norm_req), many=True)
        return Response(data=ser.data)
