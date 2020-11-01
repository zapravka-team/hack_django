import pandas as pd
from pet.models import Pet, Treatment, Vaccination, HealthStatus, Breed, PetGender, ColorType, FursType, EarType, TailType, \
    SizeType, PetType, EuthanasiaCause, SterilizationType, DisposeCause
from authentication.models import Vet
from manufacture.models import AdministrativeRegion, Shelter
import dateparser
from django.conf import settings
import os
import re


def is_nan(num): return num != num


def str_or_none(field):
    return str(field).strip().lower() if not is_nan(field) else None


def son(field):
    return str_or_none(field)


def load_pet_from_row(row):
    if not Pet.objects.filter(accounting_card=str(row[2]).strip().lower()).exists():
        pet_type = PetType.objects.get_or_create(value=row[3])[0]
        pet = Pet(accounting_card=str(row[2]).strip().lower(), pet_type=pet_type,
                  birthdate=dateparser.parse(str(row[4])),
                  weight=float(row[5]),
                  name=son(row[6]),
                  gender=PetGender.objects.get_or_create(value=row[7].lower().strip())[0],
                  breed=Breed.objects.get_or_create(value=row[8].lower().strip(), pet_type=pet_type)[0],
                  color=ColorType.objects.get_or_create(value=row[9].lower().strip(), pet_type=pet_type)[0],
                  furs_type=FursType.objects.get_or_create(value=row[10].lower().strip(), pet_type=pet_type)[0],
                  ears_type=EarType.objects.get_or_create(value=row[11].lower().strip())[0],
                  tail_type=TailType.objects.get_or_create(value=row[12].lower().strip())[0],
                  size_type=SizeType.objects.get_or_create(value=row[13].lower().strip())[0],
                  special_parameters=son(row[14]),
                  aviary=son(row[15]), id_label=son(row[16]),
                  vet=Vet.objects.get_or_create(nlp=row[18].lower().strip())[0],
                  work_order=son(row[20]), work_order_date=dateparser.parse(str(row[21])),
                  administration_area=AdministrativeRegion.objects.get_or_create(name=row[22].lower().strip())[0],
                  catching_act=son(row[23]), catching_address=son(row[24]),
                  recipient_date=dateparser.parse(str(row[37])),
                  recipient_act=son(row[38]), disposals_date=dateparser.parse(str(row[39])),
                  disposals_cause=None if isinstance(row[40], float) else
                  DisposeCause.objects.get_or_create(value=str(row[40]))[0],
                  contract_act=None if isinstance(row[40], float) else str(row[40]))
        try:
            st_date = dateparser.parse(str(row[17]))
            pet.sterilization_date = st_date
            pet.sterilization_status = SterilizationType.objects.get_or_create(value='стерелизовано')[0]
        except Exception:
            pet.sterilization_status = SterilizationType.objects.get_or_create(value=row[17].lower().strip())[0]
        pet.socialized = row[19].strip().lower() == 'да'

        pet.save()
    else:
        pet = Pet.objects.get(accounting_card=str(row[2]).strip().lower())
    return pet


def load_xlsx():
    data = pd.read_excel(os.path.join(settings.BASE_DIR, 'db_load/DataSet.xlsx'), header=1)

    for i, pet_row in enumerate(data.itertuples()):
        pet = load_pet_from_row(pet_row)
        raw_numbers = pet_row[46]
        raw_date = pet_row[47]
        raw_product_name = pet_row[48]
        raw_dose = pet_row[49]
        if isinstance(raw_numbers, int):
            treatment = Treatment(number=int(pet_row[46]), date=dateparser.parse(str(pet_row[47])),
                                  product_name=pet_row[48].strip(),
                                  dose=son(pet_row[49]), pet=pet).save()
        else:
            numbers = re.split(r'\s+', raw_numbers)
            dates = list(map(dateparser.parse, re.split(r"\s+", son(raw_date))))
            product_names = re.split(r"\s+", raw_product_name)
            doses = re.split("\s+", raw_dose)
            for i in range(min(len(numbers), len(dates), len(product_names), len(doses))):
                Treatment(number=numbers[i], date=dates[i],
                          product_name=product_names[i],
                          dose=doses[i], pet=pet).save()

        number = pet_row[50]
        dates = pet_row[51]
        vac_types = pet_row[52]
        serial_number = pet_row[53]
        if isinstance(number, int):
            Vaccination(number=son(pet_row[50]), date=dateparser.parse(str(pet_row[51])),
                        vac_type=son(pet_row[52]),
                        serial_number=son(pet_row[53]), pet=pet).save()
        else:
            numbers = re.split(r'\s+', str(number))
            dates = list(map(dateparser.parse, re.split(r'\s+', str(dates))))
            vac_types = re.split(r'\s+', str(vac_types))
            serial_numbers = re.split(r'\s+', str(serial_number))
            for i in range(min(len(numbers), len(dates), len(vac_types), len(serial_number))):
                Vaccination(number=numbers[i], date=dates[i],
                            vac_type=vac_types[i],
                            serial_number=serial_numbers[i], pet=pet).save()
