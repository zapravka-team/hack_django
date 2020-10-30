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

    def to_internal_value(self, data):
        ret = super().to_internal_value(data)
        print(ret)

        return ret

    def to_representation(self, instance):
        return {
            'кличка': instance.name,
            'тип шерсти': instance.pet_type.key,
        }

    class Meta:
        model = Pet
        fields = '__all__'
