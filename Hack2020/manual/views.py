from rest_framework.generics import ListAPIView


from manufacture.serializers import ShelterSerializerLight, OperationOrganizationSerializer
from pet.serializer import PetTypeSerializer, PetGenderSerializer, BreadSerializer, ColorTypeSerializer, \
    FursTypeSerializer, EarTypeSerializer, TailTypeSerializer, DeathCauseSerializer, DisposeCauseSerializer, \
    EuthanasiaCauseSerializer
from pet.models import Bread
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
    parser_classes = PetGenderSerializer
    queryset = PetGender.objects.all()


class BreedsView(ListAPIView):
    parser_classes = BreadSerializer
    queryset = Bread.objects.all()


class ColorsView(ListAPIView):
    parser_classes = ColorTypeSerializer
    queryset = ColorType.objects.all()


class FursTypesView(ListAPIView):
    parser_classes = FursTypeSerializer
    queryset = FursType.objects.all()


class EarTypesView(ListAPIView):
    parser_classes = EarTypeSerializer
    queryset = EarType.objects.all()


class TailTypesView(ListAPIView):
    parser_classes = TailTypeSerializer
    queryset = TailType.objects.all()


class DeathCausesView(ListAPIView):
    parser_classes = DeathCauseSerializer
    queryset = DeathCause.objects.all()


class DisposalCauseView(ListAPIView):
    parser_classes = DisposeCauseSerializer
    queryset = DisposeCause.objects.all()


class EuthanasiaCauseBookView(ListAPIView):
    parser_classes = EuthanasiaCauseSerializer
    queryset = EuthanasiaCause.objects.all()