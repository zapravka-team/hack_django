import pandas as pd
from .models import Pet, Treatment, Vaccination, HealthStatus, Breed, PetGender, ColorType, FursType, EarType, TailType, \
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


def load_xlsx():
    data = pd.read_excel(os.path.join(settings.BASE_DIR, 'pet/DataSet.xlsx'), header=1)

    for i, pet_row in enumerate(data.itertuples()):
        print(i)
        pet_type = PetType.objects.get_or_create(value=pet_row[3])[0]
        if not Pet.objects.filter(accounting_card=str(pet_row[2]).strip().lower()).exists():
            pet = Pet(accounting_card=str(pet_row[2]).strip().lower(), pet_type=pet_type,
                      birthdate=dateparser.parse(str(pet_row[4])),
                      weight=float(pet_row[5]),
                      name=son(pet_row[6]),
                      gender=PetGender.objects.get_or_create(value=pet_row[7].lower().strip())[0],
                      breed=Breed.objects.get_or_create(value=pet_row[8].lower().strip(), pet_type=pet_type)[0],
                      color=ColorType.objects.get_or_create(value=pet_row[9].lower().strip(), pet_type=pet_type)[0],
                      furs_type=FursType.objects.get_or_create(value=pet_row[10].lower().strip, pet_type=pet_type)[0],
                      ears_type=EarType.objects.get_or_create(value=pet_row[11].lower().strip())[0],
                      tail_type=TailType.objects.get_or_create(value=pet_row[12].lower().strip())[0],
                      size_type=SizeType.objects.get_or_create(value=pet_row[13].lower().strip())[0],
                      special_parameters=son(pet_row[14]),
                      aviary=son(pet_row[15]), id_label=son(pet_row[16]),
                      vet=Vet.objects.get_or_create(nlp=pet_row[18].lower().strip())[0],  # socialized=pet_row[19],
                      work_order=son(pet_row[20]), work_order_date=dateparser.parse(str(pet_row[21])),
                      administration_area=AdministrativeRegion.objects.get_or_create(name=pet_row[22].lower().strip())[
                          0],
                      catching_act=son(pet_row[23]), catching_address=son(pet_row[24]),
                      recipient_date=dateparser.parse(str(pet_row[37])),
                      recipient_act=son(pet_row[38]), disposals_date=dateparser.parse(str(pet_row[39])),
                      disposals_cause=None if isinstance(pet_row[40], float) else
                      DisposeCause.objects.get_or_create(value=str(pet_row[40]))[0],
                      death_cause=None,
                      euthanasia_cause=None, contract_act=None if isinstance(pet_row[40], float) else str(pet_row[40]))
            try:
                st_date = dateparser.parse(str(pet_row[17]))
                pet.sterilization_date = st_date
                pet.sterilization_status = SterilizationType.objects.get_or_create(value='стерелизовано')[0]
            except Exception:
                pet.sterilization_status = SterilizationType.objects.get_or_create(value=pet_row[17].lower().strip())[0]
            pet.socialized = pet_row[19].strip().lower() == 'да'

            pet.save()
        else:
            pet = Pet.objects.get(accounting_card=str(pet_row[2]).strip().lower())
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
                treatment = Treatment(number=numbers[i], date=dates[i],
                                      product_name=product_names[i],
                                      dose=doses[i], pet=pet).save()

        number = pet_row[50]
        dates = pet_row[51]
        vac_types = pet_row[52]
        serial_number = pet_row[53]
        if isinstance(number, int):
            vaccination = Vaccination(number=int(pet_row[50]), date=dateparser.parse(str(pet_row[51])),
                                      vac_type=pet_row[52].strip(),
                                      serial_number=int(pet_row[53]), pet=pet).save()
        else:
            numbers = re.split(r'\s+', number)
            dates = list(map(dateparser.parse, re.split(r'\s+', dates)))
            vac_types = re.split(r'\s+', vac_types)

        #         health_status = HealthStatus(inspection_date=dateparser.parse(str(pet_row[54])), anamnesis=pet_row[55].strip(),
        #                                      pet=pet).save()
        # # #
        # for pet_row in data.itertuples():
        #     pet = Pet(accounting_card=pet_row[2], pet_type=pet_row[3], birthdate=pet_row[4], weight=pet_row[5], name=pet_row[6],
        #               gender=PetGender.objects.get_or_create(pet_row[7].lower().strip()),
        #               bread=Bread.objects.get_or_create(pet_row[8].lower().strip()),
        #               color=ColorType.objects.get_or_create(pet_row[9].lower().strip()),
        #               furs_type=FursType.objects.get_or_create(pet_row[10].lower().strip),
        #               ears_type=EarType.objects.get_or_create(pet_row[11].lower().strip()),
        #               tail_type=TailType.objects.get_or_create(pet_row[12].lower().strip()),
        #               size_type=SizeType.objects.get_or_create(pet_row[13].lower().strip()), special_parameters=pet_row[14],
        #               aviary=pet_row[15], id_label=pet_row[16], sterilization_date=pet_row[17],
        #               vet=Vet.objects.get_or_create(pet_row[18].lower().strip()), socialized=pet_row[19],
        #               work_order=pet_row[20], work_order_date=pet_row[21],
        #               administration_area=AdministrativeRegion.objects.get_or_create(pet_row[22].lower().strip()),
        #               catching_act=pet_row[23], catching_address=pet_row[24], recipient_date=pet_row[37],
        #               recipient_act=pet_row[38], disposals_date=pet_row[39], disposals_cause=pet_row[40], death_cause=None,
        #               euthanasia_cause=None, contract_act=pet_row[41])
        #     pet.save()
        # #38 и 39
        #     pet = Treatment(number=pet_row[46], date=pet_row[47], vac_type=pet_row[48], dose=pet_row[49]).save()
        #     pet = Vaccination(number=pet_row[50], date=pet_row[51], vac_type=pet_row[52], serial_number=pet_row[53]).save()
        #     pet = HealthStatus(inspection_date=pet_row[54], anamnesis=pet_row[55]).save()
