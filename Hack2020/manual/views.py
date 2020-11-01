from rest_framework.generics import ListAPIView
from manufacture.serializers import ShelterSerializerLight, OperationOrganizationSerializer
from pet.serializer import PetTypeSerializer, PetGenderSerializer, BreedSerializer, ColorTypeSerializer, \
    FursTypeSerializer, EarTypeSerializer, TailTypeSerializer, DeathCauseSerializer, DisposeCauseSerializer, \
    EuthanasiaCauseSerializer
from pet.models import Breed
from manufacture.models import Shelter, OperatingOrganization
from pet.models import PetType, PetGender, ColorType, FursType, EarType, TailType, DeathCause, DisposeCause, \
    EuthanasiaCause
from rest_framework.permissions import IsAuthenticated

class SheltersView(ListAPIView):
    serializer_class = ShelterSerializerLight
    queryset = Shelter.objects


class OpOrgsView(ListAPIView):
    serializer_class = OperationOrganizationSerializer
    queryset = OperatingOrganization.objects


class PetTypesView(ListAPIView):
    serializer_class = PetTypeSerializer
    queryset = PetType.objects


class PetGendersView(ListAPIView):
    serializer_classes = PetGenderSerializer
    queryset = PetGender.objects


class BreedsView(ListAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects


class ColorsView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ColorTypeSerializer
    queryset = ColorType.objects


class FursTypesView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FursTypeSerializer
    queryset = FursType.objects


class EarTypesView(ListAPIView):
    serializer_classes = EarTypeSerializer
    queryset = EarType.objects


class TailTypesView(ListAPIView):
    serializer_class = TailTypeSerializer
    queryset = TailType.objects


class DeathCausesView(ListAPIView):
    serializer_classes = DeathCauseSerializer
    queryset = DeathCause.objects


class DisposalCauseView(ListAPIView):
    serializer_class = DisposeCauseSerializer
    queryset = DisposeCause.objects


class EuthanasiaCauseBookView(ListAPIView):
    serializer_class = EuthanasiaCauseSerializer
    queryset = EuthanasiaCause.objects
