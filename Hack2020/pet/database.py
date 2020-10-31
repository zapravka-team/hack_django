import pandas as pd
from .models import Pet, Treatment, Vaccination, HealthStatus, Bread, PetGender, ColorType, FursType, EarType, TailType, \
    SizeType
from authentication.models import Vet
from manufacture.models import AdministrativeRegion, Shelter

data = pd.read_excel('./DataSet.xlsx', header=1)
print(data.head())
for pet_row in data.itertuples():
    pet = Pet(accounting_card=pet_row[1], pet_type=pet_row[2], birthdate=pet_row[3], weight=pet_row[4], name=pet_row[5],
              gender=PetGender.objects.get_or_create(pet_row[6].lower().strip()),
              bread=Bread.objects.get_or_create(pet_row[7].lower().strip()),
              color=ColorType.objects.get_or_create(pet_row[8].lower().strip()),
              furs_type=FursType.objects.get_or_create(pet_row[9].lower().strip),
              ears_type=EarType.objects.get_or_create(pet_row[10].lower().strip()),
              tail_type=TailType.objects.get_or_create(pet_row[11].lower().strip()),
              size_type=SizeType.objects.get_or_create(pet_row[12].lower().strip()), special_parameters=pet_row[13],
              aviary=pet_row[14], id_label=pet_row[15], sterilization_date=pet_row[16],
              vet=Vet.objects.get_or_create(pet_row[17].lower().strip()), socialized=pet_row[18],
              work_order=pet_row[19], work_order_date=pet_row[20],
              administration_area=AdministrativeRegion.objects.get_or_create(pet_row[21].lower().strip()),
              catching_act=pet_row[22], catching_address=pet_row[23], recipient_date=pet_row[36],
              recipient_act=pet_row[38], disposals_date=pet_row[39], disposals_cause=pet_row[40], death_cause=None,
              euthanasia_cause=None, contract_act=pet_row[41])
    pet.save()

    pet = Treatment(number=pet_row[46], date=pet_row[47], vac_type=pet_row[48], dose=pet_row[49]).save()
    pet = Vaccination(number=pet_row[50], date=pet_row[51], vac_type=pet_row[52], serial_number=pet_row[53]).save()
    pet = HealthStatus(inspection_date=pet_row[54], anamnesis=pet_row[55]).save()
