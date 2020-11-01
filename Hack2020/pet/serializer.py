from rest_framework.serializers import ModelSerializer
import rest_framework.serializers as ser

from .models import Pet, HealthStatus, Vaccination, Treatment, PetType, ColorType, FursType, TailType, EarType, \
    DeathCause, PetGender, Breed, DisposeCause, EuthanasiaCause
from authentication.serializers import VetSerializer, CaregiverSerializer, PetOwnerSerializer
from manufacture.serializers import ShelterSerializer


class EuthanasiaCauseSerializer(ModelSerializer):
    class Meta:
        model = EuthanasiaCause
        exclude = ['id']


class DisposeCauseSerializer(ModelSerializer):
    class Meta:
        model = DisposeCause
        exclude = ['id']


class ColorTypeSerializer(ser.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def to_representation(self, instance):
        ret = {}
        for pet_type in PetType.objects.all():
            ret[pet_type.value] = ColorType.objects.values_list('value', flat=True).filter(pet_type=pet_type)
        return ret


class FursTypeSerializer(ser.Serializer):

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def to_representation(self, instance):
        ret = {}
        for pet_type in PetType.objects.all():
            ret[pet_type.value] = FursType.objects.values_list('value', flat=True).filter(pet_type=pet_type)
        return ret


class TailTypeSerializer(ModelSerializer):
    class Meta:
        model = TailType
        exclude = ['id']


class EarTypeSerializer(ModelSerializer):
    class Meta:
        model = EarType
        exclude = ['id']


class DeathCauseSerializer(ModelSerializer):
    class Meta:
        model = DeathCause
        exclude = ['id']


class PetGenderSerializer(ModelSerializer):
    class Meta:
        model = PetGender
        exclude = ['id']


class BreedSerializer(ser.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def to_representation(self, instance):
        ret = {}
        for pet_type in PetType.objects.all():
            ret[pet_type.value] = Breed.objects.values_list('value', flat=True).filter(pet_type=pet_type)
        return ret


class PetTypeSerializer(ModelSerializer):
    class Meta:
        model = PetType
        fields = ['value']


class HealthStatusSerializer(ser.ModelSerializer):
    class Meta:
        model = HealthStatus
        exclude = ['id', 'pet']


class VaccinationSerializer(ser.ModelSerializer):
    class Meta:
        model = Vaccination
        exclude = ['id', 'pet']


class TreatmentSerializer(ser.ModelSerializer):
    class Meta:
        model = Treatment
        exclude = ['id', 'pet']


class PetSmartSerializer(ser.Serializer):
    pass


class PetSerializer(ser.ModelSerializer):
    color = ser.CharField(source='color.value')
    breed = ser.CharField(source='breed.value')
    pet_type = ser.CharField(source='pet_type.value')
    furs_type = ser.CharField(source='furs_type.value')
    ears_type = ser.CharField(source='ears_type.value')
    tail_type = ser.CharField(source='tail_type.value')
    size_type = ser.CharField(source='size_type.value')
    gender = ser.CharField(source='gender.value')
    disposals_cause = ser.CharField(source='disposals_cause.value', default='')
    death_cause = ser.CharField(source='death_cause.value', default='')
    euthanasia_cause = ser.CharField(source='euthanasia_cause.value', default='')
    administration_area = ser.CharField(source='administration_area.name', default='')
    vet = VetSerializer()
    caregiver = CaregiverSerializer()
    shelter = ShelterSerializer()
    owner = PetOwnerSerializer()
    vaccination = VaccinationSerializer(many=True)
    treatment = TreatmentSerializer(many=True)
    heath_history = HealthStatusSerializer(many=True, source='health_status')

    class Meta:
        model = Pet
        exclude = ['id']
