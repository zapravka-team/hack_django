from django.contrib import admin

from .models import Pet, PetType, SizeType, FursType, TailType, EarType, ColorType, Vaccination, Treatment, Bread

# Register your models here.

admin.site.register(Pet)
# admin.site.register(PetOwner)
    # admin.site.register(AdministrationArea)
admin.site.register(Bread)
admin.site.register(PetType)
admin.site.register(SizeType)
admin.site.register(FursType)
admin.site.register(TailType)
admin.site.register(EarType)
admin.site.register(ColorType)
admin.site.register(Vaccination)
admin.site.register(Treatment)
