from django.contrib import admin

# Register your models here.
from .models import PetOwner, Vet, Caregiver

admin.site.register(PetOwner)
admin.site.register(Vet)
admin.site.register(Caregiver)