import pandas as pd
from .models import Pet, Treatment, Vaccination, HealthStatus, Breed, PetGender, ColorType, FursType, EarType, TailType, \
    SizeType, PetType, EuthanasiaCause, SterilizationType
from authentication.models import Vet
from manufacture.models import AdministrativeRegion, Shelter
import dateparser
from django.conf import settings
import os


def load_xlsx():
    data = pd.read_excel(os.path.join(settings.BASE_DIR, 'pet/DataSet.xlsx'), header=1)

    for pet_row in data.itertuples():
        pet_type = PetType.objects.get_or_create(value=pet_row[3].strip().lower())[0]
        print(pet_row[1])
        print(pet_row[14])
        print(pet_row[15])
        pet = Pet(accounting_card=pet_row[2], pet_type=pet_type, birthdate=dateparser.parse(pet_row[4]),
                  weight=float(pet_row[5]), name=pet_row[6],
                  gender=PetGender.objects.get_or_create(value=pet_row[7].lower().strip())[0],
                  bread=Breed.objects.get_or_create(value=pet_row[8].lower().strip(), pet_type=pet_type)[0],
                  color=ColorType.objects.get_or_create(value=pet_row[9].lower().strip(), pet_type=pet_type)[0],
                  furs_type=FursType.objects.get_or_create(value=pet_row[10].lower().strip(), pet_type=pet_type)[0],
                  ears_type=EarType.objects.get_or_create(value=pet_row[11].lower().strip())[0],
                  tail_type=TailType.objects.get_or_create(value=pet_row[12].lower().strip())[0],
                  size_type=SizeType.objects.get_or_create(value=pet_row[13].lower().strip())[0],
                  special_parameters=pet_row[14].strip(),
                  aviary=int(pet_row[15].strip()), id_label=pet_row[16].strip(),
                  # sterilization_date=dateparser.parse(pet_row[16]),
                  vet=Vet.objects.get_or_create(nlp=pet_row[18].lower().strip())[0],
                  work_order=pet_row[19].strip(), work_order_date=dateparser.parse(pet_row[20]),
                  administration_area=AdministrativeRegion.objects.get_or_create(name=pet_row[21].lower().strip())[0],
                  catching_act=pet_row[22].strip(), catching_address=pet_row[23].strip(),
                  recipient_date=dateparser.parse(pet_row[36].strip()), recipient_act=pet_row[38].strip(),
                  disposals_date=dateparser.parse(pet_row[39]), disposals_cause=pet_row[40], death_cause=None,
                  euthanasia_cause=None, contract_act=pet_row[41].strip())
        try:
            st_date = dateparser.parse(pet_row[17].strip())
            pet.sterilization_date = st_date
            pet.sterilization_status = SterilizationType.objects.get_or_create(value='стерелизовано')[0].id
        except Exception:
            pet.sterilization_status = SterilizationType.objects.get_or_create(value=pet_row[16].lower().strip())
        pet.socialized = pet_row[18].strip().lower() == 'да'

        pet.save()
        treatment = Treatment(number=int(pet_row[46].strip()), date=dateparser.parse(pet_row[47]),
                              product_name=pet_row[48].strip(),
                              dose=pet_row[49].strip(), pet=pet.id).save()
        vaccination = Vaccination(number=int(pet_row[50].strip()), date=dateparser.parse(pet_row[51]),
                                  vac_type=pet_row[52].strip(),
                                  serial_number=int(pet_row[53].strip()), pet=pet.id).save()
        health_status = HealthStatus(inspection_date=dateparser.parse(pet_row[54]), anamnesis=pet_row[55].strip(),
                                     pet=pet.id).save()
