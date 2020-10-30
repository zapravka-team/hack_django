from rest_framework.serializers import ModelSerializer
import rest_framework.serializers as ser
from .models import Pet


class PetSerializer(ModelSerializer):

    #name = ser.CharField(label='кличка', )

    class Meta:
        model = Pet
        fields = '__all__'