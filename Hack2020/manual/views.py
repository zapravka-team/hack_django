from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from manufacture.serializers import ShelterSerializerLight, OperationOrganizationSerializer
from pet.serializer import PetTypeSerializer, PetGenderSerializer, BreedSerializer, ColorTypeSerializer, \
    FursTypeSerializer, EarTypeSerializer, TailTypeSerializer, DeathCauseSerializer, DisposeCauseSerializer, \
    EuthanasiaCauseSerializer
from pet.models import Breed
from manufacture.models import Shelter, OperatingOrganization
from pet.models import PetType, PetGender, ColorType, FursType, EarType, TailType, DeathCause, DisposeCause, \
    EuthanasiaCause


class SheltersView(ListAPIView):
    serializer_class = ShelterSerializerLight
    queryset = Shelter.objects.all()

    def post(self, request, *args, **kwargs):
        return


class OpOrgsView(ListAPIView):
    serializer_class = OperationOrganizationSerializer
    queryset = OperatingOrganization.objects.all()


class PetTypesView(ListAPIView):
    serializer_class = PetTypeSerializer
    queryset = PetType.objects.all()


class PetGendersView(ListAPIView):
    serializer_classes = PetGenderSerializer
    queryset = PetGender.objects.all()


class BreedsView(APIView):

    def get(self, request, *args, **kwargs):
        cats = BreedSerializer(Breed.objects.filter(pet_type__value='кошка'), many=True)
        dogs = BreedSerializer(Breed.objects.filter(pet_type__value='собака'), many=True)
        return Response(data={'cats': cats.data, 'dogs': dogs.data})


class ColorsView(APIView):
    def get(self, request, *args, **kwargs):
        cats = ColorTypeSerializer(ColorType.objects.filter(pet_type__value='кошка'), many=True)
        dogs = ColorTypeSerializer(ColorType.objects.filter(pet_type__value='собака'), many=True)
        return Response(data={'cats': cats.data, 'dogs': dogs.data})


class FursTypesView(APIView):

    def get(self, request, *args, **kwargs):
        cats = FursTypeSerializer(FursType.objects.filter(pet_type__value='кошка'), many=True)
        dogs = FursTypeSerializer(FursType.objects.filter(pet_type__value='собака'), many=True)
        return Response(data={'cats': cats.data, 'dogs': dogs.data})


class EarTypesView(ListAPIView):
    serializer_classes = EarTypeSerializer
    queryset = EarType.objects.all()


class TailTypesView(ListAPIView):
    serializer_class = TailTypeSerializer
    queryset = TailType.objects.all()


class DeathCausesView(ListAPIView):
    serializer_classes = DeathCauseSerializer
    queryset = DeathCause.objects.all()


class DisposalCauseView(ListAPIView):
    serializer_class = DisposeCauseSerializer
    queryset = DisposeCause.objects.all()


class EuthanasiaCauseBookView(ListAPIView):
    serializer_class = EuthanasiaCauseSerializer
    queryset = EuthanasiaCause.objects.all()
