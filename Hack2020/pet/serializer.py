from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer
import rest_framework.serializers as ser
from .models import Pet, HealthStatus, Vaccination, Treatment

from authentication.serializers import VetSerializer, CaregiverSerializer, PetOwnerSerializer
from manufacture.serializers import ShelterSerializer
# class PetTypeSerializer(ModelSerializer):
#     class Meta:
#         model = PetType
#         fields = ['key']
#
#
# class CustomSerializer(ModelSerializer):
#     ...
#
#
# class PetSerializer(ModelSerializer):
#
#     def to_internal_value(self, data):
#         ret = super().to_internal_value(data)
#         print(ret)
#
#         return ret
#
#     def to_representation(self, instance):
#         return {'id': instance.accounting_card,
#                 'общие сведения': {
#             'вид': instance.pet_type.key,
#             'возраст': instance.birthdate,
#             'вес': instance.weight,
#             'кличка': instance.name,
#             'пол': instance.gender,
#             'порода': instance.bread.key,
#             'окрас': instance.color.key,
#             'шерсть': instance.pet_type.key,
#             'уши': instance.ears_type.key,
#             'хвост': instance.tail_type.key,
#             'размер': instance.size_type.key,
#             'особые приметы': instance.special_parameters,
#             'Вольер №': instance.aviary,
#             },
#                 "дополнительные сведения": {
#                     'идентификационная метка': instance.id_label,
#                     #стерилизовано
#                     'дата стерилизации': instance.sterilization_date,
#                     'ф.и.о. ветеринарного врача': instance.vet_nlp,
#                     'Социализировано': instance.socialized
#                 },
#                 "сведения об отлове": {
#                     "заказ-наряд / акт о поступлении животного №": instance.work_order,
#                     #"заказ-наряд дата/ акт о поступлении животного, дата": instance.
#                     "административный округ": instance.administration_area.key,
#                     "акт отлова №": instance.catching_act,
#                     "адрес места отлова": instance.catching_address
#                 },
#                 "сведения о новых владельцах": [{
#                     "юридическое лицо": instance.,
#                     "ф.и.о. опекунов": instance.,
#                     "физическое лицо ф.и.о.": instance.
#                 }],
#                 "движение животного": {
#                     "дата поступления в приют": instance.,
#                     "акт №": instance.,
#                     "дата выбытия из приюта": instance.,
#                     "причина выбытия": instance.,
#                     "акт/договор №": instance.
#                 },
#                 "ответственные за животное": {
#                     "адрес приюта": instance.,
#                     "эксплуатирующая организация": instance.,
#                     "ф.и.о. руководителя приюта": instance.,
#                     "ф.и.о. сотрудника по уходу за животным": instance.
#                 },
#                 "сведения об обработке от экто- и эндопаразитов": [{
#                     "№ п/п": instance.,
#                     "дата": instance.,
#                     "название препарата": instance.,
#                     "доза": instance.
#                 }],
#                 "сведения о вакцинации": [{
#                     "№ п/п": instance.,
#                     "дата": instance.,
#                     "вид вакцины": instance.,
#                     "№ серии": instance.
#                 }],
#                 "сведения о состоянии здоровья": {
#                     "дата осмотра": instance.,
#                     "анамнез": instance.
#                 }
#         }
#
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework.serializers import HyperlinkedRelatedField


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
    bread = ser.CharField(source='bread.value')
    pet_type = ser.CharField(source='pet_type.value')
    furs_type = ser.CharField(source='furs_type.value')
    ears_type = ser.CharField(source='ears_type.value')
    tail_type = ser.CharField(source='tail_type.value')
    size_type = ser.CharField(source='size_type.value')
    gender = ser.CharField(source='gender.value')
    disposals_cause = ser.CharField(source='disposals_cause.value')
    death_cause = ser.CharField(source='death_cause.value')
    euthanasia_cause = ser.CharField(source='euthanasia_cause.value')
    administration_area = ser.CharField(source='administration_area.name')
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
