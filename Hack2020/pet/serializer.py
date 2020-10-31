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


class ColorTypeSerializer(ModelSerializer):
    class Meta:
        model = ColorType
        fields = ['value']


class FursTypeSerializer(ModelSerializer):
    class Meta:
        model = FursType
        fields = ['value']


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


class BreedSerializer(ModelSerializer):
    class Meta:
        model = Breed
        fields = ['value']


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
