from rest_framework.serializers import ModelSerializer
import rest_framework.serializers as ser
from .models import Pet, PetType


class PetTypeSerializer(ModelSerializer):
    class Meta:
        model = PetType
        fields = ['key']


class CustomSerializer(ModelSerializer):
    ...


class PetSerializer(ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
    def to_internal_value(self, data):
        ret = super().to_internal_value(data)
        print(ret)

        return ret

    def to_representation(self, instance):
        return {'id': instance.accounting_card,
                'общие сведения': {
            'вид': instance.pet_type.key,
            'возраст': instance.birthdate,
            'вес': instance.weight,
            'кличка': instance.name,
            'пол': instance.gender,
            'порода': instance.bread.key,
            'окрас': instance.color.key,
            'шерсть': instance.pet_type.key,
            'уши': instance.ears_type.key,
            'хвост': instance.tail_type.key,
            'размер': instance.size_type.key,
            'особые приметы': instance.special_parameters,
            'Вольер №': instance.aviary,
            },
                "дополнительные сведения": {
                    'идентификационная метка': instance.id_label,
                    #стерилизовано
                    'дата стерилизации': instance.sterilization_date,
                    'ф.и.о. ветеринарного врача': instance.vet_nlp,
                    'Социализировано': instance.socialized
                },
                "сведения об отлове": {
                    "заказ-наряд / акт о поступлении животного №": instance.work_order,
                    #"заказ-наряд дата/ акт о поступлении животного, дата": instance.
                    "административный округ": instance.administration_area.key,
                    "акт отлова №": instance.catching_act,
                    "адрес места отлова": instance.catching_address
                },
                "сведения о новых владельцах": [{
                    "юридическое лицо": instance.id,
                    "ф.и.о. опекунов": instance.id,
                    "физическое лицо ф.и.о.": instance.id
                }],
                "движение животного": {
                    "дата поступления в приют": instance.recipient_date,
                    "акт №": instance.recipient_act,
                    "дата выбытия из приюта": instance.disposals_date,
                    "причина выбытия": instance.disposals_cause,
                    "акт/договор №": instance.contract_act
                },
                "ответственные за животное": {
                    "адрес приюта": instance.id,
                    "эксплуатирующая организация": instance.id,
                    "ф.и.о. руководителя приюта": instance.id,
                    "ф.и.о. сотрудника по уходу за животным": instance.id
                },
                "сведения об обработке от экто- и эндопаразитов": [{
                    "№ п/п": instance.id,
                    "дата": instance.id,
                    "название препарата": instance.id,
                    "доза": instance.id
                }],
                "сведения о вакцинации": [{
                    "№ п/п": instance.number,
                    "дата": instance.date,
                    "вид вакцины": instance.vac_type,
                    "№ серии": instance.serial_number
                }],
                "сведения о состоянии здоровья": {
                    "дата осмотра": instance.id,
                    "анамнез": instance.id
                }
        }

